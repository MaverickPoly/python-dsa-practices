from math import gcd
from functools import reduce


def solution(array):
    res = reduce(gcd, array)
    return res
    # return res * len(array)


print(solution([6, 12, 9, 18]))


