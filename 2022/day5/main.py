import os
import array

def parse():
    path = os.path.dirname(os.path.abspath(__file__)) + "/stack.txt"

    stacks = []
    with open(path) as file:
        for line in file.read().splitlines():
            stackForIndex = line.strip()[:-1:][::-1]
            stacks.append([container for container in stackForIndex])

    return stacks

def main():
    path = os.path.dirname(os.path.abspath(__file__)) + "/input.txt"

    stack1 = parse()
    stack2 = parse()

    with open(path) as file:
        for move in file.read().splitlines():
            part1(stack1, move)
            part2(stack2, move)
        
    print("part1", "".join([stack[-1] for stack in stack1]))
    print("part2", "".join([stack[-1] for stack in stack2]))
    
def part1(stacks, move):
    count, fromIndex, toIndex = list(map(int,move.split(" ")))
    for i in range(0, count):
        stacks[toIndex-1].append(stacks[fromIndex-1].pop())
  
def part2(stacks, move):
    count, fromIndex, toIndex = list(map(int,move.split(" ")))
    sFrom = stacks[fromIndex-1]
    movable = sFrom[len(sFrom) - count::]

    print("from", stacks[fromIndex-1])
    print("to", stacks[toIndex-1])

    for i in movable:
        stacks[fromIndex-1].pop()
        stacks[toIndex-1].append(i)
    
    print("from", stacks[fromIndex-1])
    print("to", stacks[toIndex-1])

if __name__=="__main__":
    main()