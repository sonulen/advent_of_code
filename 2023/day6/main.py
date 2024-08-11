import itertools
import os
import array


def lowerBound(array, check):
    left = 0
    right = len(array) - 1

    while left < right:
        midIndex = (left + right) // 2
        midValue = array[midIndex]
        if check(midValue):
            right = midIndex
        else:
            left = midIndex + 1

    return left

def upperBound(array, check):
    left = 0
    right = len(array) - 1

    while left < right:
        midIndex = (left + right + 1) // 2
        midValue = array[midIndex]
        if check(midValue):
            left = midIndex
        else:
            right = midIndex - 1

    return left

def answer(races):
    wins = 1
    for (time, distance) in races.items():
        firstWinTime = lowerBound(
            array = [*range(1, time + 1)],
            check = lambda x: (time - x) * x > distance
        )
        lastWinTime = upperBound(
            array = [*range(1, time + 1)],
            check = lambda x: (time - x) * x > distance
        ) + 1

        wins *= (lastWinTime - firstWinTime)

    return wins


def main():
    # Time / distance
    testRaces = {
        7: 9,
        15: 40,
        30: 200
    }
    races_part1 = {
        40: 233,
        82: 1011,
        84: 1110,
        92: 1487
    }

    races_part2 = {
        40828492 : 233101111101487
    }

    print(f"Part1 {answer(races_part1)} \n Part2 {answer(races_part2)}")



if __name__=="__main__":
    main()