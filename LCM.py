
"""
Question 6
Least Common Multiple in Python [Python Algorithm Performance Facebook Programming]

The least common multiple of a set of integers is the smallest positive integer that is a multiple of all of the
integers in the set.
Write a function that takes an array of integers and efficiently calculates and returns the LCM.

"""
def lcm(*values):
	values = set([abs(int(v)) for v in values])
	if values and 0 not in values:
		n = n0 = max(values)
		values.remove(n)
		while any( n % m for m in values ):
			n += n0
		return n
	return 0


print lcm(5,6,10,15,12)