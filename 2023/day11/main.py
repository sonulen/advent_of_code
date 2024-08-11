import os

def main():
    path = os.path.dirname(os.path.abspath(__file__)) + "/input.txt"
    with open(path) as file:
        galaxy = file.read()
        galaxyCount = galaxy.count('#')
        

    print(f"Part1 {0} \n Part2 {0}")



if __name__=="__main__":
    main()