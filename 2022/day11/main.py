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
        self.items = items
        self.operation = operation
        self.test = test
        self.inspected = 0

    def appendItems(self, items):
        for item in items:
            self.items.append(item)
    
    def turn(self):
        if len(self.items) == 0:
            return []
        
        items = [int(eval(self.operation.replace("old", str(item)))) // 3 for item in self.items]
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
        
    part1(monkeys, rounds = 20)

def part1(monkeys, rounds):
    for i in range(1, rounds + 1):
        print("Round", i)
        for monkey in monkeys:
            moveableItems = monkey.turn()

            if len(moveableItems) == 0:
                continue

            for id, items in moveableItems:
                monkeys[id].appendItems(items)

        print("after round#", i, monkeys)
        


if __name__=="__main__":
    main()