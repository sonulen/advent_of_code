import itertools
import os
import array


def main():
    path = os.path.dirname(os.path.abspath(__file__)) + "/input.txt"
    # part1(path)
    part2(path)
         
def part1(path):
    part1sum = 0
    with open(path) as file:
        for line in file:
            onlyDigits = ''.join(filter(str.isdigit, line))
            if (len(onlyDigits)) < 2:
                onlyDigits = onlyDigits[0] + onlyDigits[0]
            part1sum += int(onlyDigits[0]) * 10 + int(onlyDigits[-1])
            
    print("Part1 = " , part1sum)

def part2(path):
 partb = 0;
 with open(path) as f:
  for l in f:
    sofar = '';
    line = l.strip()

    first = '';
    last = '';
    for c in line:
      sofar += c;
      if 'one' in sofar: c = '1' ; sofar = '';
      if 'two' in sofar: c = '2' ; sofar = '';
      if 'three' in sofar: c = '3' ; sofar = '';
      if 'four' in sofar: c = '4' ; sofar = '';
      if 'five' in sofar: c = '5' ; sofar = '';
      if 'six' in sofar: c = '6' ; sofar = '';
      if 'seven' in sofar: c = '7' ; sofar = '';
      if 'eight' in sofar: c = '8' ; sofar = '';
      if 'nine' in sofar: c = '9' ; sofar = '';

      if c in '0123456789':
        sofar = '';
        if first == '':
          first = int(c);

    rev_line = line[::-1]
    sofar = '';
    for c in rev_line:
      sofar = c + sofar;
      if 'one' in sofar: c = '1' ; sofar = '';
      if 'two' in sofar: c = '2' ; sofar = '';
      if 'three' in sofar: c = '3' ; sofar = '';
      if 'four' in sofar: c = '4' ; sofar = '';
      if 'five' in sofar: c = '5' ; sofar = '';
      if 'six' in sofar: c = '6' ; sofar = '';
      if 'seven' in sofar: c = '7' ; sofar = '';
      if 'eight' in sofar: c = '8' ; sofar = '';
      if 'nine' in sofar: c = '9' ; sofar = '';

      if c in '0123456789':
        sofar = '';
        if last == '':
          last = int(c);

    value_string = str(first) + str(last);
    value = int(value_string);
    partb += value;
    
 print("Part2 = ", partb)
            

if __name__=="__main__":
    main()