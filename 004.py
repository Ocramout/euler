from itertools import combinations_with_replacement
def function(n):
    # 9009
    c = combinations_with_replacement(range(900, 1000), 2)
    d = list(c)
    d.reverse()
    for a,b in d:
        pal = str(a*b)
        lap = pal[::-1]
        if pal == lap:
            print(a, b, a*b)
            
function(3)
