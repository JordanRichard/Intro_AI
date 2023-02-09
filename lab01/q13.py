s = "This is right justified"
def mysplit(s):
	lst = []
	tmp = ""
	for c in s:
		if c != " ":
			tmp = tmp + c
		else:
			lst.append(tmp)
			tmp = ""
	if tmp != "":
		lst.append(tmp)
		tmp = ""
	return lst

print(mysplit(s))
