def cut(n):
    # 13195
    # 600851475143
    res = []
    for i in range(2, int(n**2)):
        if i*i > n: break
        while n%i == 0:
            n //= i
            res += [i]
    if n > 1:
        res += [n]
    return res

print(cut(600851475143))

