def permutations(l, l2=[]):
	if len(l) <= 1:
		perms.append(l2+l)
		return
	for i in range(len(l)):
		permutations(l[:i]+l[i+1:], l2+[l[i]])

perms = []
l = [1,2,3]
permutations(l)
print(perms)
