def power(x, y):
	if y==0:
		return 1
	tmp = power(x, int(y/2))
	if y%2 == 0:
		return tmp*tmp
	return x*tmp*tmp

print(power(2,3))
