import itertools
import os
import array


def main():
    path = os.path.dirname(os.path.abspath(__file__)) + "/input.txt"

    with open(path) as file:
        forest = parse(file.read())
        
    print(part1(forest))
    print(part2(forest))

def parse(content):
    forest = []

    for line in content.splitlines():
        forest.append(line)

    return forest

def part1(forest):
    result = 0
    for rowIndex, line in enumerate(forest):
        if rowIndex == 0 or rowIndex == len(forest) -1:
                result+=len(line)
                continue

        for columnIndex, tree in enumerate(line):
            if columnIndex == 0 or columnIndex == len(line) -1:
                result += 1
                continue

            top = max([forest[index][columnIndex] for index in range(0,rowIndex)])
            left = max([forest[rowIndex][index] for index in range(0, columnIndex)])
            right = max([forest[rowIndex][index] for index in range(columnIndex + 1, len(forest[rowIndex]))])
            bottom = max([forest[index][columnIndex] for index in range(rowIndex + 1, len(forest))])

            if tree > top or tree > left or tree > right or tree > bottom:
                result += 1
    
    return result


def part2(forest):
    result = 0

    print(forest)
    for rowIndex, line in enumerate(forest):
        if rowIndex == 0 or rowIndex == len(forest) -1:
                continue

        print("line", line)

        for columnIndex, tree in enumerate(line):
            tree = int(tree)

            if columnIndex == 0 or columnIndex == len(line) -1:
                continue

            top = [int(forest[index][columnIndex]) for index in range(0,rowIndex)]
            left = [int(forest[rowIndex][index]) for index in range(0, columnIndex)]
            right = [int(forest[rowIndex][index]) for index in range(columnIndex + 1, len(forest[rowIndex]))]
            bottom = [int(forest[index][columnIndex]) for index in range(rowIndex + 1, len(forest))]

            if tree > max(top) or tree > max(left) or tree > max(right) or tree > max(bottom):
                top.reverse()
                left.reverse()
                visibility = visible(tree, top) * visible(tree, left) * visible(tree, right) * visible(tree,bottom)
                result = max(visibility, result)
    
    return result

def visible(tree, anotherTrees):
    result = 0
    for currentTree in anotherTrees:
        if tree > currentTree:
            result += 1
        else:
            result += 1
            break

    if result == 0:
        result = 1
    
    return result


if __name__=="__main__":
    main()