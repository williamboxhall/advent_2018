#!/usr/bin/python3
import sys, itertools, functools, time, collections

with open(sys.argv[1]) as input:
	deltas = itertools.cycle(map(int, input.readlines()))
	sums1, sums2 = itertools.tee(itertools.accumulate(deltas, lambda x,y: x+y))
	seen = itertools.chain([set()], itertools.accumulate(map(lambda x: {x}, sums1), lambda x,y: x.union(y)))
	zipped = zip(seen, sums2)
	dups = map(lambda x: x[1], filter(lambda x: x[1] in x[0], zipped))
	print(next(dups))