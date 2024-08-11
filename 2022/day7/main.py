import itertools
import os
import array


def main():
    path = os.path.dirname(os.path.abspath(__file__)) + "/input.txt"

    with open(path) as file:
        content = file.read()
        solution(content)   

def solution(output):
    stack, sizes = [], []
    for line in output.splitlines():
        if line == '$ cd ..':
            size = stack.pop()
            sizes.append(size)
            stack[-1] += size
        elif line.startswith('$ cd '):
            stack.append(0)
        elif line[0].isdigit():
            stack[-1] += int(line.split()[0])

    print("stacks", stack)
    print("sizes", sizes)

    sizes.extend(itertools.accumulate(stack[::-1]))

    print("sizes after", sizes)
    print("stacks", stack)

    print("part1", sum(s for s in sizes if s <= 100_000))
    print("part2", min(s for s in sizes if s >= max(sizes) - 40_000_000))


if __name__=="__main__":
    main()