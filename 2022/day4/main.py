import os

def main():
    path = os.path.dirname(os.path.abspath(__file__)) + "/input.txt"
    with open(path) as file:
        score = 0
        for task in file.read().splitlines():
            score += part1(task)
        print("part1", score)

    
    with open(path) as file:
        score = 0
        for task in file.read().splitlines():
            score += part2(task)
        print("part2", score)

def check1(section, intersect):
    
    if (intersect is None or len(intersect) == 0):
        return False

    return section[0] >= intersect[0] and section[1] <= intersect[-1]

# A X- Камень 1
# B Y- Бумага 2
# С Z- Ножницы 3
def part1(task: str):
    sections = [section.split("-") for section in task.split(',')]
    first = list(map(lambda x: int(x), sections[0]))
    second = list(map(lambda x: int(x), sections[1]))

    intersect = list(range(max(first[0], second[0]), min(first[-1], second[-1])+1))
    intersect.sort()

    result = int((check1(first, intersect) or check1(second, intersect)))

    return result

# A = Камень 1  X = lose
# B = Бумага 2  Y = draw
# С = Ножницы 3 Z = win    
def part2(task: str):
    sections = [section.split("-") for section in task.split(',')]
    first = list(map(lambda x: int(x), sections[0]))
    second = list(map(lambda x: int(x), sections[1]))

    intersect = set(range(first[0], first[1] + 1)).intersection(range(second[0], second[1]+1))

    result = int(len(intersect) != 0)

    print("first", first, "second", second, "intersect", intersect, "result", result)

    return result

if __name__=="__main__":
    main()