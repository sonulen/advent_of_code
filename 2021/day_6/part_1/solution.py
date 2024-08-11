#!/usr/bin/python3


class Lanternfish:
    def __init__(self, days):
        self.lifeCounter = days

    def iteration(self):
        self.lifeCounter -= 1
        if self.lifeCounter < 0:
            self.lifeCounter = 6
            return Lanternfish(8)

        return None

    def __repr__(self):
        return "{}".format(self.lifeCounter)


with open("input.txt") as f:
    fishes = f.readline().strip().split(",")

fish_generation = [Lanternfish(int(fish)) for fish in fishes]

days = 256

for i in range(1, days + 1):
    childs = []
    for fish in fish_generation:
        child = fish.iteration()
        if child:
            childs.append(child)
    fish_generation.extend(childs)

print(len(fish_generation))
