def fn(n):
	for i in range(10):
		if i > n:
			return True
	return False

print(fn(3))
print(fn(10))
