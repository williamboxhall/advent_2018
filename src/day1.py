#!/usr/bin/python
import sys

with open(sys.argv[1]) as input:
	all_lines = input.readlines()
	all_numbers = map(int, all_lines)
	total = sum(all_numbers)
	print total