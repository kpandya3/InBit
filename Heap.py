def Heapify(l, fun):
	def HeapifyHelper(l, k):
		m = fun(l[k], l[2*k+1], l[2*k+2])

		if m != l[k]:
			tmp = l[k]
			if l[2*k+1] == m:
				l[k] = l[2*k+1]
				l[2*k+1] = tmp
			else:
				l[k] = l[2*k+2]
				l[2*k+2] = tmp

	n = int(math.log(len(l) - 1, 2))

	for i in range(n+1, 0, -1):
		HeapifyHelper(l, i-1)
	return l

print(Heapify([7,4,8,3,6,8,2], max))

def HeapInsert(l, val, fun):
	def ShiftUp(l, i):
		parent = int((i-2)/2) if i%2==0 else int((i-1)/2)
		m = fun(l[parent], l[i])
		if m == l[i]:
			tmp = l[i]
			l[i] = l[parent]
			l[parent] = tmp
			if parent != 0:
				ShiftUp(l, parent)

	l.append(val)
	ShiftUp(l, len(l)-1)
	return l

def HeapDel(l, i, fun):
	del l[i]

	Heapify(l, fun)

l = [7,4,8,3,6,8,2]

print(HeapDel(l, 0, max))
