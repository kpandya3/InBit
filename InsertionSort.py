def InsertionSort(l):
	for i in range(1, len(l)):
		val = l[i]
		j = i - 1
		while (j >= 0) and (l[j] > val):
			l[j+1] = l[j]
			j = j - 1
		l[j+1] = val
	return l

print(InsertionSort([6,34,5,82,54,8,2,1,0,9,4]))