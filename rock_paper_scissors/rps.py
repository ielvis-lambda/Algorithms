#!/usr/bin/python

import sys


def rock_paper_scissors(n):
		rps = ["rock", "paper", "scissors"]
		allPlays = [['game']]
		plays = [allPlays * 3**((n))]
		print(f"I'm the plays: {plays}")
		if n <= 0:
				return plays
		for roundNumber in range(n, n+1):
				print(f" i'm the round: {roundNumber}")
				print(f" i'm allPlays: {allPlays}")
				if n == 1:
						allPlays = [['rock'], ['paper'], ['scissors']]
						pass
				else:
						for n in range(n, n+1):
							print(f" round {n}")
							for i in rps:
								allPlays.append(i)
							print(f"test allPlays {allPlays}")
						# for i in allPlays:
						# 		for j in range(0,3):
						# 			# allplays
						# 			i.append(rps[j])
						# 			print(f"I'm testttt allPlays {allPlays}")
						# 			pass

		print(f" i'm Final allPlays: {allPlays}")
		return allPlays


if __name__ == "__main__":
		if len(sys.argv) > 1:
				num_plays = int(sys.argv[1])
				print(rock_paper_scissors(num_plays))
		else:
				print('Usage: rps.py [num_plays]')
