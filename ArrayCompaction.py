
"""
Question 3
 Array Compaction in Python [Python Algorithm Easy Microsoft Programming]

Write a function that takes as input a sorted array and modifies the array to compact it, removing duplicates. Also
return the new length of the array.

Notes: The input array might be very large.

For example:

input array = [1, 3, 7, 7, 8, 9, 9, 9, 10]
transformed array = [1, 3, 7, 8, 9, 10]
size = 6

"""
def removeDuplicate(items):
    return len(list(set(items)))

print removeDuplicate([1, 3, 7, 7, 8, 9, 9, 9, 10])