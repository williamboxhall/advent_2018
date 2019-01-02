#!/usr/bin/python
import sys

with open("day1input.txt") as input:
	all_lines = input.readlines()
	all_numbers = map(lambda x: int(x), all_lines)
	total = sum(all_numbers)
	print total