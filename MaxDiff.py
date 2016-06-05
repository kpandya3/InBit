# Given an array, find the maximum difference between two array elements given the second element comes after the first.

def MaxDiff(l):
	MaxDiff = l[1] - l[0]
	minElement = l[0]

	for i in range(1, len(l)):
		if l[i] - minElement > MaxDiff:
			MaxDiff = l[i] - minElement
		if l[i] < minElement:
			minElement = l[i]
	return MaxDiff

l = [2,3,212,2,3,5,21,1,3,46,2,3,4,54,3,4,23,4,32,5,234,23,4,23]

print(MaxDiff(l))
