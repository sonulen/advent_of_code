import os, re, math

def part1(steps, nodeMap):
    stepsCount = 0
    target = "ZZZ"
    current = "AAA"

    while current != target:
        turn = steps[stepsCount % len(steps)]
        current = nodeMap[current][0] if turn == "L" else nodeMap[current][1]
        stepsCount += 1

    return stepsCount


def part2(steps, nodeMap):
    stepsCount = 0
    stepsToFinish = []
    currents = {k: v for k, v in nodeMap.items() if k.endswith('A')}

    while len(currents) != 0:
        turn = steps[stepsCount % len(steps)]

        newCurrents = {}
        for _, turns in currents.items():
            nextNode = turns[0] if turn == "L" else turns[1]

            if nextNode.endswith('Z'):
                stepsToFinish.append(stepsCount + 1)
            else:
                newCurrents[nextNode] = nodeMap[nextNode]
        
        currents = newCurrents
        stepsCount += 1

    return math.lcm(*stepsToFinish)       


def main():
    # path = os.path.dirname(os.path.abspath(__file__)) + "/test.txt"
    path = os.path.dirname(os.path.abspath(__file__)) + "/input.txt"
    with open(path) as file:
        steps = file.readline().strip()
        print("steps = ", len(steps))
        nodeMap = {}
        for line in file.read().splitlines():
            pattern = re.compile(r"(.*) = \((.*), (.*)\)") 
            match = pattern.match(line)
            nodeMap[match.group(1)] = [match.group(2), match.group(3)]

    print(f"Part 1 = {part1(steps, nodeMap)}")
    print(f"Part2 = {part2(steps, nodeMap)}")


if __name__=="__main__":
    main()