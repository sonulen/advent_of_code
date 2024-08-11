#!/usr/bin/python

def main():
    with open("input.txt") as f:
        positions = [int(pos) for pos in f.read().strip().split(",")]

    fuel_costs_map = []
    for target_position in range(len(positions)):
        fuel_cost = sum([abs(position-target_position) for position in positions])
        fuel_costs_map.append(fuel_cost)

    print("Part 1 answer = {}".format(min(fuel_costs_map)))


if __name__ == "__main__":
    main()
