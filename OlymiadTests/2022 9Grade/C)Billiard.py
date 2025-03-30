"""
Given the length and width of the billiard table, we need to find to which hole the ball enters 
and how many hits it will make, if it turns by 45%.
"""
from math import gcd

def billiard(length, width):
    lcm = length * width // gcd(length, width)
    kx = lcm // length
    ky = lcm // width
    hits = width + length - 2

    if kx % 2 == 0 and ky % 2 == 0:
        hole = 1
    elif kx % 2 == 0 and ky % 2 != 0:
        hole = 4
    elif kx % 2 != 0 and ky % 2 == 0:
        hole = 2
    else:
        hole = 3

    return hits, hole


length, width = map(int, input().split())
hits, hole = billiard(length, width)
print(hits, hole)
    
