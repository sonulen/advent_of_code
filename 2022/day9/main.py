import itertools
import os
import array

def direction(coordTo, coordFrom):
    x = coordTo - coordFrom
    return min(max(x, -1), 1)

class Point:
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y

    def move(self, dir): 
        match(dir):
            case("U"): self.y += 1
            case("D"): self.y -= 1
            case("R"): self.x += 1
            case("L"): self.x -= 1

class Rope:
    def __init__(self, lenght): #create 10 knot rope
        self.knots=[]
        for i in range(lenght):
            self.knots.append(Point())
            
    def move_next(self, head, tail): #move tail knot after head knot 
        if abs(head.x - tail.x) > 1 or abs(head.y - tail.y) > 1:
            tail.x += direction(head.x, tail.x)
            tail.y += direction(head.y, tail.y)
            return True
        else:
            return False
            
    def move_rope(self): # move every knot from 1 to 9 (not the head)
        for i in range(1, len(self.knots)):
            if not self.move_next(self.knots[i-1],self.knots[i]):
                break

def main():
    path = os.path.dirname(os.path.abspath(__file__)) + "/input.txt"

    with open(path) as file:
        moves = file.read()
        
    print(part(moves,2))
    print(part(moves, 10))

def part(moves, ropeLenght):
    rope = Rope(ropeLenght)
    visited = []

    for line in moves.splitlines():
        dir, count = line.split(" ")
        for i in range(int(count)):
            rope.knots[0].move(dir)
            rope.move_rope()
            visited.append(tuple[rope.knots[-1].x, rope.knots[-1].y])

    return len(set(visited))



if __name__=="__main__":
    main()