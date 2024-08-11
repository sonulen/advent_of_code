import os
import array

def main():
    path = os.path.dirname(os.path.abspath(__file__)) + "/input.txt"

    with open(path) as file:
        for message in file.read().splitlines():
            print("part1", part1(message))
            print("part2", part2(message))
        
    
def part1(message):
    marker = []
    for i in range(0, len(message)):
        symbol = message[i]
        marker.append(symbol)
        
        if len(marker) == 4:
            if len(set(marker)) == 4:
                print("index" , i, marker)
                return i + 1
            
            marker = marker[1::]
 
    return 0
  
def part2(message):
    marker = []
    for i in range(0, len(message)):
        symbol = message[i]
        marker.append(symbol)
        
        if len(marker) == 14:
            if len(set(marker)) == 14:
                print("index" , i, marker)
                return i + 1
            
            marker = marker[1::]
 
    return 0

if __name__=="__main__":
    main()