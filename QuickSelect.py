def QuickSelect(l, n):
	if len(l) == 1:
		return l[0]
	rightList = [i for i in l if i > l[0]] 
	leftList = [i for i in l if i < l[0]] 
	
	if n == len(leftList):
		return l[0]
	if n < len(leftList):
		return QuickSelect([i for i in l if i < l[0]], n)
	return QuickSelect(rightList, n-(len(l)-len(rightList)))

print(QuickSelect([6,34,5,82,54,8,2,1,0,9,4],5))