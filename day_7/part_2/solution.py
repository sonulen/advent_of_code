#!/usr/bin/python


def calculate_fuel_cost(distance):
    return distance * (distance + 1) / 2
    return sum(range(distance + 1))

def main():
    with open("input.txt") as f:
        positions = [int(pos) for pos in f.read().strip().split(",")]

    fuel_costs_map = []
    for target_position in range(len(positions)):
        distances = [abs(position-target_position) for position in positions]
        fuel_costs = [calculate_fuel_cost(distance) for distance in distances]
        fuel_cost = sum(fuel_costs)
        fuel_costs_map.append(fuel_cost)

    print("Part 2 answer = {}".format(min(fuel_costs_map)))


if __name__ == "__main__":
    main()
