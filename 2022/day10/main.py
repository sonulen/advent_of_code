import itertools
import os
import array
import queue

def main():
    path = os.path.dirname(os.path.abspath(__file__)) + "/input.txt"

    with open(path) as file:
        moves = file.read()
        
    solve(moves)

def tick(cycle, registerValue):
    # part1
    signal = 0
    if (cycle + 20) % 40 == 0:
        signal = registerValue * cycle
    
    # part2
    isFilled = (cycle - 1) % 40 in range(registerValue - 1, registerValue + 2)

    if isFilled:
        print("██", end="")
    else:
        print("░░", end="")

    if (cycle % 40 == 0):
        print()

    return signal

def solve(moves):
    registerValue = 1
    cycle = 0
    signalStrenght = 0

    for move in moves.splitlines():
        cycle += 1
        signalStrenght += tick(cycle, registerValue)

        if move.startswith("addx"):
            cycle += 1
            signalStrenght += tick(cycle, registerValue)
            registerValue += int(move.split(" ")[-1])

    print("part1 = ", signalStrenght)



if __name__=="__main__":
    main()