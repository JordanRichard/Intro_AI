def isprime(n,divisor):
	if n < 2:
		return False

		if (n == divisor):
			return True
	elif (n % divisor == 0):
		return False
	
	return isprime(n,divisor-1)


if __name__ == "__main__":
	print(isprime(2,2))
