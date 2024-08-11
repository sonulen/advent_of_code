#!/usr/bin/python

from typing import List


counter: int = 0
numbers = []
with open('input.txt') as f:
    for line in f:
        numbers.append(int(line.strip()))

numbers_sum = []

prev: int = sum(numbers[0:3])
counter: int = 0
for index in range(1,len(numbers) - 2):
    current: int = sum(numbers[index:index+3])
    if current > prev:
        counter += 1
    prev = current

print(counter)