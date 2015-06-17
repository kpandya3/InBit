def MergeSort(l):
	if len(l) == 1:
		return l
	head = MergeSort(l[:int(len(l)/2)])
	tail = MergeSort(l[int(len(l)/2):])
	return Merge(head, tail)

def Merge(l1, l2):
	# While l1/l2 left
	if l1 and not l2:
		return l1
	if l2 and not l1:
		return l2
	if l1[0] > l2[0]:
		return l2[:1] + Merge(l1, l2[1:])
	return l1[:1] + Merge(l1[1:], l2)


print(MergeSort([6,34,2,5,6,82,2,54,8,2,1,0,9,4]))