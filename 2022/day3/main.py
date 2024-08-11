import os

from collections import Counter

lower =  {chr(i+96):i for i in range(1,27)}
upper =  {chr(i+38):i for i in range(27,53)} 

print("lower", lower)
print("upper", upper)

def main():
    path = os.path.dirname(os.path.abspath(__file__)) + "/input.txt"
    with open(path) as file:
        score = 0
        for backpack in file.read().splitlines():
            score += part1(backpack)
        print("part1", score)
    
    with open(path) as file:
        score = 0
        with open(path) as file:
            backpacks = [line for line in file.read().splitlines()]

        for i in range(0, len(backpacks), 3):
            elfs = [backpacks[i] for i in range(i,i+3)]
            score += part2(elfs)

        print("part2", score)

# A X- Камень 1
# B Y- Бумага 2
# С Z- Ножницы 3
def part1(backpack):
    score = 0
    left = backpack[:len(backpack) // 2]
    right = backpack[len(backpack) // 2:]
    
    intersect = set(left).intersection(right)
    for char in intersect:
        score += lower.get(char,0) + upper.get(char, 0)

    return score 

# A = Камень 1  X = lose
# B = Бумага 2  Y = draw
# С = Ножницы 3 Z = win    
def part2(elfsBackpacks):
    score = 0
    intersect = set(elfsBackpacks[0]).intersection(elfsBackpacks[1]).intersection(elfsBackpacks[2])
    
    for char in intersect:
        score += lower.get(char,0) + upper.get(char, 0)

    return score

if __name__=="__main__":
    main()