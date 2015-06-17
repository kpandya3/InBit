def Factorial(n):
	return n if n==1 else n*Factorial(n-1)

print(Factorial(5))
