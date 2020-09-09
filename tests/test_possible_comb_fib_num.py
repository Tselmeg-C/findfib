import pytest
from findfib.PossibleCombOfFibNum import PossibleCombOfFibNum

def test_get_fib_num_list():
	expected = [2, 3, 5, 8, 13, 21, 34, 55, 89]

	upper_limit = 100
	ff = PossibleCombOfFibNum(upper_limit)
	actual = ff.fibonacci_numbers
	
	assert(actual==expected)

def test_get_fib_num_combination_sum_to_target():
	expected = 	[[2, 2, 2, 2, 3], [8, 3],[2, 2, 2, 5], [2, 3, 3, 3], [3, 3, 5]]
	expected = [sorted(e) for e in sorted(expected)]

	target = 11
	ff = PossibleCombOfFibNum(target)
	ff.find_fib_combinations_sum_to_target()
	actual = ff.fib_combinations_sum_to_target
	actual = [sorted(e) for e in sorted(actual)]

	assert(actual==expected)
	