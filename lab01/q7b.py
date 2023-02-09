m = [x for x in range(10) if x%3 == 1]
n = [x for x in range(10) if x%3 == 2]
y = [t*u for t in m for u in n]
print(sum(y))
