class Vector:
	def __init__(self,lst):
		self.vec = lst

	def __repr__(self):
		return "Vector({0})".format(self.vec)

	def __add__(self,other):
		return Vector([self.vec[i] + other.vec[i]
			for i in range(len(self.vec))])
x = Vector([1,2,3])
print(x + x)
