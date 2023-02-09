def f(n):
	if n<=2:
		return 1
	else:
		return f(n-1) + g(n-2)
		
def g(n):
	if n<=2:
		return 1
	else:
		return f(n-1) + g(n-2)
		
print(f(10))
