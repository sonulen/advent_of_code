#!/usr/bin/python

counter = 0

with open('input.txt') as f:
    prev = int(f.readline().strip())
    for line in f:
        number = int(line.strip())
        if number > prev:
            counter+=1
        prev = number

print(counter)