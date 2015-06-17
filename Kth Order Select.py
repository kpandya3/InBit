def KthOrderSelect(l, k):

	if len(l) == 1:
		return l[0]
	medians = []
	for i in range(0, int(len(l)/5)):
		medians.append(l[(i*5)+2])
	medians.append(l[len(medians)*5 + int((len(l)%5)/2)])

	pivot = KthOrderSelect(medians, math.ceil(int(len(l)/10)))

	leftList = [i for i in l if i< pivot]
	rightList = [i for i in l if i>= pivot]
	if len(leftList)+1 == k:
		return pivot
	if len(leftList) > k:
		return KthOrderSelect(leftList, k)
	return KthOrderSelect(rightList, k-len(leftList))

print(KthOrderSelect([7,4,3,7,3,2,9,0,3,11,34,6,4,45,7,654,6,54,34,5,6,35,4,5,435,4,5,9,43,5,43,5,345,6547,87,769,89], 10))