#!/usr/bin/python

field = [0 for i in range(0,1000 * 1000,1)]

def fill_points(x, y, xx, yy):
    if x == xx and y == yy:
        return
    
    if (x == xx):
        for y in range(min(y, yy), max(y, yy)+1):
            field[x + y * 1000] += 1
    elif (y == yy):
        for x in range(min(x, xx), max(x, xx)+1):
            field[x + y * 1000] += 1
    else:
        if x > xx:
            x_direction = -1
        else:
            x_direction = +1

        if y > yy:
            y_direction = -1
        else:
            y_direction = +1
        
        for i in range(0, abs(x - xx) + 1):
            new_x = x + (i * x_direction)
            new_y = y + (i * y_direction)
            field[new_x + new_y * 1000] += 1

with open('input.txt') as f:
    for line in f:
        x,y, xx, yy = [int(x) for x in line.strip().replace(' -> ', ",").split(",")]
        fill_points(x, y, xx, yy)


min_value = 2
counter = 0

for point in field:
    if point >= 2:
        counter += 1

print("Result = ", counter)