def somme(n):
    if n < 10:
        return n
    return sum([int(i) for i in str(n)])
def function(n):
    a = 1
    for i in range(n-1):
        if (i%10**6 == 0):
            print("completion: {:.7%}".format(i/10**15))
        a += somme(a)
    return a

#print(function(10**15))
#31054319
#1000000 de boucle en 5sec

n = 10**15
a = 1
for i in range(n-1):
    if (i%10**6 == 0):
        print("completion: {:.7%}".format(i/10**15))
    a += sum([int(x) for x in str(i)])
print(a)