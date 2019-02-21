#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):
    if n == 0:
      return 1
    elif n == 1:
      return 1
    ways = [0] * (n + 1)
    # print(ways)
    ways[0] = 1
    ways[1] = 1
    ways[2] = 2

    for i in range(3, n + 1):
        print(f"i is {i}")
        ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3]

    return ways[n]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')
