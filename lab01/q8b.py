n = 10
def f(n):
	print('local(f) n =',n)
	
def g():
	global n
	n = 20
	print('local(g) n =',n)
print('global n =', n)
f(15)
print('global n = ',n)
g()
print('global n = ', n)
