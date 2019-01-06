#!/usr/bin/python3
import sys, itertools, functools, time, collections

with open(sys.argv[1]) as input:
	#deltas = itertools.cycle(map(int, input.readlines()))
	counter = 0 

	def timed(x):
		global counter
		counter += 1
		print(counter)
		return x

	deltas = map(timed, itertools.cycle(map(int, input.readlines())))
	#deltas = itertools.cycle([1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16])
	#deltas = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16]
	#deltas_cycled = itertools.cycle(deltas)
	#deltas_cycled = deltas

	# todo start with zero?
	#deltas = itertools.chain([0], deltas)
	sums = itertools.accumulate(itertools.chain([0], deltas), lambda x,y: x+y)
	seen = itertools.accumulate(itertools.chain([set()], map(lambda x: {x}, sums)), lambda x,y: x.union(y))
	zipped = zip(seen, sums)
	dups = filter(lambda x: x[1] in x[0], zipped)
	print(next(dups))


    # def deltas = Iterator.continually(data).flatten
    # def sums = deltas.scanLeft(0)(_ + _)
    # def seen = sums.scanLeft(Set.empty)(_ + _)
    # def dups = (seen zip sums).filter(_ contains _).map((_, sum) => sum)
    # print(dups.next)


	# frequencies_and_empty_counts = map(lambda x: (x, collections.defaultdict(lambda: 0, {})), frequencies)

	# def reducer(old, new):
	# 	old_freq = old[0]
	# 	new_freq = new[0]
	# 	old_dict = old[1]
	# 	new_dict = new[1]

	# 	updated_dict = old_dict.copy()
	# 	if (old_dict[old_freq] == 0):
	# 		updated_dict[old_freq] = 1
	# 	updated_dict[new_freq] += 1

	# 	print(len(updated_dict))

	# 	return (new_freq, collections.defaultdict(lambda: 0, updated_dict))

	# frequencies_and_counts = itertools.accumulate(frequencies_and_empty_counts, reducer)
	# counts = map(lambda x: x[1], frequencies_and_counts)

	# def duplicate_frequencies(counts): #map in, list of dupes out. needs ifilter?
	# 	dupe_items = filter(lambda x: x[1] > 1, counts.items())
	# 	values = list(map(lambda x: x[0], dupe_items))

	# 	return values

	# duplicates = map(duplicate_frequencies, counts)

	# def predicate(dupe_list): # this is a map like {1: 1, 2: 2, 3: 1}
	# 	return len(dupe_list) > 0

	# first_duplicate = next(x for x in duplicates if predicate(x))

	# print("done")
	# print(first_duplicate)


	#def pred2(item):
	#	return item[1] > 1

	#def predicate(counts): # this is a map like {1: 1, 2: 2, 3: 1}
	#	entries = counts.items()
	#	print(entries)

	#	return item in entries if pred2(item)

	#first_duplicate = next(x for x in counts if predicate(x))
	#print(first_duplicate)	


	#times_seen = itertools.reduce(reducer, seen_and_frequencies, (frozenset(), 0))


	#for item in frequencies:
	#	print(item)
	#	time.sleep(1)

	#def foo(previous, delta):
	#	frequency = previous + delta
	#	if frequency in seen:
	#		print frequency
	#		exit
	#	else:



	#reduce(foo, deltas_acc)
	#def find_revisited_frequency(ds, previous_frequency, seen):
	#	print next(ds)
	#	frequency = next(ds) + previous_frequency
	#	if frequency in seen:
	#		return None, frequency
	#	else:
	#		return find_revisited_frequency, (ds, frequency, seen.union(frozenset([frequency])))

	