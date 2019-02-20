#!/usr/bin/python

import argparse

def find_max_profit(prices):
	maxProfit = [0]
	for b in range(0, len(prices)):
		for s in range(prices.index(prices[b]), len(prices)):
			profit = prices[s] - prices[b]
			if profit > maxProfit[0]:
				temp = profit
				maxProfit[0] = temp
			# print (prices[s])
			# print(maxProfit)
		# print (prices[b])
	return maxProfit[0]
	# pass

# prices = [1050, 270, 1540, 3800, 2]

# find_max_profit(prices)

if __name__ == '__main__':
	# This is just some code to accept inputs from the command line
	parser = argparse.ArgumentParser(description='Find max profit from prices.')
	parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
	args = parser.parse_args()

	print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))