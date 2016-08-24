from math import sqrt
import itertools


def F(a=9, b=10, c=11):
    x, y, z = 360/a, 360/b, 360/sqrt(c)
    #x, y, z = 60, 60, 60

    flips = 0
    turns = 0
    angle1 = 0
    angle2 = 0
    angles = []
    pieces = (x, y, z)
    TOP = True
    cake_360 = [TOP for _ in range(360)]

    # le plus grand angle possible 109
    while flips < 60:
        if (turns == 0):
            while True:
                next_piece = pieces[flips%3]
                angle2 += next_piece
                flips += 1

                if angle2 >= 360:
                    turns += 1
                    angle1 = angle2
                    
                    if angle2 == 360:
                        print('angle2 == 360')
                        cake_360 = [False for _ in range(360)]
                        break
                    else:
                        turns += 1
                        angle2 -= next_piece
                        angle1 = angle2
                        for i in range(angle2):
                            cake_360[i] = False
                        break

        else:
            angle2 = (angle1 + pieces[flips%3])
            flips += 1
            
            if angle2 >= 360:
                angle2 = angle2%360
                turns += 1


    return flips



def G(n):
    res = 0
    for x in combinations(n):
        res += F()
    print(res)

def combinations(n):
    return itertools.combinations(range(9, n+1), 3)

G(11)
