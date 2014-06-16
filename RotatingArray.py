
"""
Question 5
Rotating an Array in Python
Write a function that takes an array of integers and returns that array rotated by N positions.
For example, if N=2, given the input array [1, 2, 3, 4, 5, 6] the function should return [5, 6, 1, 2, 3, 4]
"""
def rotateArrayByNPlaces(inputList, n):
    return [inputList[(i-n) % len(inputList)] for i in range(len(inputList))]
print rotateArrayByNPlaces([1, 2, 3, 4, 5, 6], 2)