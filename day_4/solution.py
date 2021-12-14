#!/usr/bin/python

class Field:
    def __init__(self, value) -> None:
        self.value = value
        self.isMarked = False

    def __str__(self):
        return "Field with value = {} isMarked = {}".format(self.value, self.isMarked)

    def __unicode__(self):
        return u"Field with value = {} isMarked = {}".format(self.value, self.isMarked)

    def __repr__(self):
        return "Field with value = {} isMarked = {}".format(self.value, self.isMarked)


class Table:
    def __init__(self) -> None:
        self.table = []

    def append(self, value):
        self.table.append(value)

    def find_and_set(self, example):
        for i, row in enumerate(self.table):
            for j, field in enumerate(row):
                if (field.value == example):
                    field.isMarked = True
                    return (i,j)

        return None

    def row(self, index):
        return self.table[index]

    def column(self, index):
        column = []
        for i, row in enumerate(self.table):
            for j, value in enumerate(row):
                if j == index:
                    column.append(value)

        return column


class Card:
    def __init__(self, board_strings):
        self.deck = Table()
        self.winner_number = None
        self.isWinner = False

        for line in board_strings:
            line_nums_str = line.replace('  ', ' ').split(' ')
            fields = [Field(x) for x in line_nums_str]
            self.deck.append(fields)

    def check(self, row):
        if all([v.isMarked for v in row]):
            return True
        return False

    def process(self, move):
        if self.isWinner:
            return False
        indexes = self.deck.find_and_set(move)
        if indexes:
            row = self.deck.row(indexes[0])
            column = self.deck.column(indexes[1])
            if self.check(row) or self.check(column):
                self.isWinner = True
                self.winner_number = int(move)
                return True        
                

    def cheer(self):
        sums_unchecked = 0
        for i, row in enumerate(self.deck.table):
            for j, field in enumerate(row):
                if not field.isMarked:
                    sums_unchecked += int(field.value)

        print("Winner = ", sums_unchecked * self.winner_number, self.winner_number)



cards = []

with open('input.txt') as f:
    moves = f.readline().strip().split(',')
    while f.readline():
        board_strings = []
        for i in range(5):
            board_strings.append(f.readline().strip())

        cards.append(Card(board_strings))

for move in moves:
    stopFlag = False
    
    for card in cards:
        if card.process(move):
            lastWinner = card
if lastWinner:
    lastWinner.cheer()

