def fn(n):
	for i in range(2,n):
		if n % i == 0:
			print(n, 'is not prime')
			return False
	print(n, 'is prime')
	return True
	
for i in range(5):
	fn(i)

