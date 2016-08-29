def fibo(n):
	a, b = 1, 2
	res = []
	while True:
		if a >= n:
			break
		elif a%2 == 0:
			res += [a]
		a, b = b, a+b
	return res

f = fibo(4000000)
print(f)
print(sum(f))