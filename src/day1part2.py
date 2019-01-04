#!/usr/bin/python
import sys, itertools

with open(sys.argv[1]) as input:
	deltas = map(int, input.readlines())
	deltas_cycled = itertools.cycle(deltas)

	frequency = 0
	seen = set()

	for delta in deltas_cycled:
		frequency = delta + frequency
		if frequency in seen:
			print("found:" + str(frequency))
			break
		else:
			print("nope:" + str(frequency))
			seen.add(frequency)

	