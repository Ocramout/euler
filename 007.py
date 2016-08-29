def checkPrime(x, primes):
	for p in primes:
		if x % p == 0:
			return False
	return True

def list_prime(n):
	primes = [2]
	i = 3
	while len(primes) < n:
		if checkPrime(i, primes):
			primes.append(i)
		i += 2
	return primes


print(list_prime(10001))
