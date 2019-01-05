#!/usr/bin/python3
import sys, itertools, functools, time, collections

with open(sys.argv[1]) as input:
	deltas = map(int, input.readlines())
	#deltas_cycled = itertools.cycle(deltas)
	deltas_cycled = deltas

	frequencies = itertools.accumulate(deltas_cycled, lambda x,y: x+y)
	frequencies_and_empty_counts = map(lambda x: (x, collections.defaultdict(lambda: 0, {})), frequencies)

	def reducer(old, new):
		old_freq = old[0]
		new_freq = new[0]
		old_dict = old[1]
		new_dict = new[1]

		new_freq_count = old_dict[new_freq] + 1
		new_freq_dict = {new_freq: new_freq_count}

		updated_dict = old_dict.copy()
		updated_dict.update(new_freq_dict)
		default_updated_dict = collections.defaultdict(lambda: 0, updated_dict)

		return (new_freq, default_updated_dict)


	frequencies_and_counts = functools.reduce(reducer, frequencies_and_empty_counts, (0, collections.defaultdict(lambda: 0, {})))
	print(frequencies_and_counts)	


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

	