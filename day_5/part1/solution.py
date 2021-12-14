#!/usr/bin/python

field = [0 for i in range(0,1000 * 1000,1)]

def fill_points(x, y, xx, yy):
    if x != xx and y != yy:
        return
    
    if (x == xx):
        for y in range(y, yy+1):
            field[x + y * 1000] += 1
    else:
        for x in range(x, xx+1):
            field[x + y * 1000] += 1


with open('input.txt') as f:
    for line in f:
        x,y, xx, yy = [int(x) for x in line.strip().replace(' -> ', ",").split(",")]
        fill_points(min(x, xx), min(y, yy), max(x, xx), max(y, yy))


min_value = 2
counter = 0

for point in field:
    if point >= 2:
        counter += 1

print("Result = ", counter)