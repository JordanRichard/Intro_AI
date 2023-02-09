def mult(i,j):
	print(i,"*",j,"=",i*j)
def right(i,j,n):
	if j < n:
		mult(i,j)
		right(i,j+1,n)
right(2,1,10)
