#!/usr/bin/python3

with open('input.txt') as f:
    prev = int(f.readline().strip())
    result = []
    maxForElf = 0
    counter = 0
    for line in f:
        inputCallories = line.strip()
        if not inputCallories or inputCallories == "":
            counter = counter + 1
            result.append(maxForElf)
            maxForElf = 0
            continue

        calls = int(line.strip())
        maxForElf += calls

result.sort(reverse=True)

print(sum(result[:3:]))