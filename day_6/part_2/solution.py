#!/usr/bin/python

from collections import Counter


def part2(fishes):
    timers = Counter({timer: 0 for timer in range(10)})
    fishes = Counter(fishes)
    fishes.update(timers)
    print(fishes)

    print(timers)

    for day in range(2):
        fishes[7] += fishes.get(0, 0)
        fishes[9] += fishes.get(0, 0)
        fishes = {fish: fishes.get(fish + 1, 0) for fish in fishes}

    return sum(fishes.values())


def main():
    with open("input.txt") as f:
        fishes = f.read().strip().split(",")
        fishes = list(map(int, fishes))

    print("Part 2 Answer: {}".format(part2(fishes)))


if __name__ == "__main__":
    main()
