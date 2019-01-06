#!/usr/bin/python
import sys, itertools

with open(sys.argv[1]) as input:
	deltas = map(int, input.readlines())
	frequency = 0
	seen = set()

	counter = 0
	for delta in itertools.cycle(deltas):
		counter += 1
		print(counter)
		frequency += delta
		if frequency in seen:
			print(frequency) #145801 steps
			break
		else:
			seen.add(frequency)
	