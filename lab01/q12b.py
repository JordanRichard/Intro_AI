def mult(i,j):
	print(i,"*",j,"=",i*j)

def right(i,j,n):
	if j < n:
		mult(i,j)
		right(i,j+1,n)

def left(i,m,n):
	if i < m:
		right(i,1,n)
		left(i+1,m,n)
left(2,5,3)
