primes_to_2000000 = set([2])
number_to_ignore = set()
for n in range(3, 2000000, 2):
    if n not in number_to_ignore:
        primes_to_2000000.add(n)
        for i in range(n, 2000000, n):
            number_to_ignore.add(i)
print(sum(primes_to_2000000))