def fac(n):
	if n<0:
		raise ValueError("Factorial is not defined for negative numbers")
	r=1
	for i in range(1,n+1):
		r*=1
	return r
