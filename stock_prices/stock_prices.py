#!/usr/bin/python

import argparse

def find_max_profit(prices):
    next = 1
    highest = prices[1]-prices[0]
    length = len(prices)
    for i in range(0, length - 1):
        for j in range(next, length):
            profit = prices[j] - prices[i]
            print("profit", profit)
            print("highest", highest)
            if profit >= highest:
                highest = profit
        next +=1
    return highest

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

# array = [10, 7, 5, 8, 11, 9]
# array = [100, 90, 80, 50, 20, 10]
# find_max_profit(array)
