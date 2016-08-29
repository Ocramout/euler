import itertools
import math
import fibo

integers = list(range(54))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
addition = list(itertools.accumulate(integers))
# [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431]
possibilities = list(itertools.accumulate(addition))
# [0, 1, 4, 10, 20, 35, 56, 84, 120, 165, 220, 286, 364, 455, 560, 680, 816, 969, 1140, 1330, 1540, 1771, 2024, 2300, 2600, 2925, 3276, 3654, 4060, 4495, 4960, 5456, 5984, 6545, 7140, 7770, 8436, 9139, 9880, 10660, 11480, 12341, 13244, 14190, 15180, 16215, 17296, 18424, 19600, 20825, 22100, 23426, 24804, 26235]

# G(53) -> 26235 possibilities
print(possibilities[-1] == sum(addition))

  ####################
  #  Arithmetic way  #
  ####################


def integers(n):
    return n

def addition(n):
    return n*(n+1)//2

def possibilities(n):
    return n*(n+1)//2*(n+2)//3


def combinations(a=9, b=53):
    
    return itertools.combinations(range(a, b+1), 3)

def G(n):
    combination = combinations()
    return sum([F(*c) for c in combination])

def F(a,b,c):
    """
    if (a, b, c)  == (9, 10, 11):
        return 60
    if (a, b, c)  == (10, 14, 16):
        return 506
    if (a, b, c)  == (15, 16, 17):
        return 785232
    """

    (x, y, z) = (360/a, 360/b, 360/math.sqrt(c))

    flips = 0
    piece = itertools.cycle( (x,y,z) )

    return flips

