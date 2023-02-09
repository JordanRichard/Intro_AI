def perm(A,start,end,i):
	if i >= end:
		print(A[start:end])
	else:
		for j in range(i,end):
			A[j],A[i] = A[i],A[j]
			perm(A,start,end,i+1)
			A[j],A[i] = A[i],A[j]
perm([1,2,3], 0, 3, 0)
