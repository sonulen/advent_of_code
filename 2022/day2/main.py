import os

def main():
    path = os.path.dirname(os.path.abspath(__file__)) + "/input.txt"
    with open(path) as file:
        rounds = [line for line in file.read().splitlines()]
            
    print(part1(rounds))
    print(part2(rounds))

# A X- Камень 1
# B Y- Бумага 2
# С Z- Ножницы 3
def part1(rounds):
    combinations = {
        "A X": 4, 
        "A Y": 8, 
        "A Z": 3,
        "B X": 1, 
        "B Y": 5, 
        "B Z": 9,
        "C X": 7, 
        "C Y": 2, 
        "C Z": 6
    }

    score = 0
    for round in rounds:
        score += combinations[round]

    return score 

# A = Камень 1  X = lose
# B = Бумага 2  Y = draw
# С = Ножницы 3 Z = win    
def part2(rounds):
    combinations = {
        "A X": 3, 
        "A Y": 4, 
        "A Z": 8,
        "B X": 1, 
        "B Y": 5, 
        "B Z": 9,
        "C X": 2, 
        "C Y": 6, 
        "C Z": 7
    }

    score = 0
    for round in rounds:
        score += combinations[round]

    return score               
    
if __name__=="__main__":
    main()