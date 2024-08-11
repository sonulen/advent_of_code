import itertools
import os
import array
import queue
import re

def partition(pred, iterable):
    trues = []
    falses = []
    for item in iterable:
        if pred(item):
            trues.append(item)
        else:
            falses.append(item)
    return trues, falses

def selfEval(operation, old: int) -> int:
    operations = operation.split(" ")

    digit1 =  operations[0]
    if digit1 == "old":
        digit1 = old
    else:
        digit1 = int(digit1)
    
    digit2 =  operations[-1]
    if digit2 == "old":
        digit2 = old
    else:
        digit2 = int(digit2)

    sign =  operations[1]
    if sign == "*":
        return digit1 * digit2
    else:
        return digit1 + digit2

class Test:
    def __init__(self, div, ifTrue, ifFalse):
        self.div = int(div)
        self.ifTrue = int(ifTrue)
        self.ifFalse = int(ifFalse)
    
    def __str__(self):
        return f"Test div {self.div} if true to #{self.ifTrue} if false to #{self.ifFalse}"
    def __repr__(self):
        return f"Test div {self.div} if true to #{self.ifTrue} if false to #{self.ifFalse}"

class Monkey:
    def __init__ (self, id, items, operation, test):
        self.id = id
        self.items = list(map(int,items))
        self.operation = operation
        self.test = test
        self.inspected = 0

    def appendItems(self, items, common_delimiter):
        for item in items:
            if item > common_delimiter:
                item %= common_delimiter
            self.items.append(item)
    
    def turn(self):
        if len(self.items) == 0:
            return []
        
        items = [selfEval(self.operation, item) for item in self.items]
        self.items = []

        trues, falses = partition(lambda x: x % self.test.div == 0, items)
        self.inspected += len(items)

        return [ (self.test.ifTrue, trues), (self.test.ifFalse, falses) ]


    def __str__(self):
        return f"Monkey#{self.id} items = {self.items} operation = {self.operation} test = {self.test}, inspected = {self.inspected}"
    def __repr__(self):
        return f"\n[Monkey#{self.id} items = {self.items} operation = {self.operation} test = {self.test}, inspected = {self.inspected}]\n"
    

def parse(input):
    monkeys = []
    for line in input.splitlines():
        id = int(re.findall("Monkey (\d+)", line)[0])
        items = re.findall("Starting items: ([0-9, ]*);", line)[0].split(", ")
        operation = re.findall("Operation: new = (.*);", line)[0]
        div, ifTrue, ifFalse = re.findall("Test: divisible by (\d*) If true: throw to monkey (\d+) If false: throw to monkey (\d*)", line)[0]

        monkeys.append(
            Monkey(
                id = id,
                items = items,
                operation = operation,
                test = Test(div, ifTrue, ifFalse)
            )
        )

    return monkeys

def main():
    path = os.path.dirname(os.path.abspath(__file__)) + "/input.txt"

    with open(path) as file:
        monkeys = parse(file.read())

    
    common_delimiter = 1

    for monkey in monkeys:
        common_delimiter *= monkey.test.div
        
    part2(monkeys = monkeys, rounds = 10000, common_delimiter = common_delimiter)

def part2(monkeys, rounds, common_delimiter):
    for i in range(1, rounds + 1):
        print("Round", i)
        for monkey in monkeys:
            moveableItems = monkey.turn()

            if len(moveableItems) == 0:
                continue

            for id, items in moveableItems:
                monkeys[id].appendItems(items, common_delimiter)

    inspected = [monkey.inspected for monkey in monkeys]
    inspected.sort()
    print(f"Part2 inspected {inspected} solution {inspected[-2] * inspected[-1]}")



if __name__=="__main__":
    main()