#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    array = []
    options = ['rock', 'paper', 'scissors']
    if n == 0:
        return [[]]
    def recursive_part(round, roundNumber):
        for i in range(0, len(options)):
            round.append(options[i])
            if roundNumber == n:
                array.append(round.copy())
            else:
                recursive_part(round, roundNumber + 1);
            round.pop()
    recursive_part([], 1)
    return array


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
# rock_paper_scissors(0)
# rock_paper_scissors(1)
# rock_paper_scissors(2)
