"""
We have a powerful king that can move two cells at once, instead of one.

v1 -> Position of the king. e.g. d4
v2 -> Target position
"""


def kingMoves(v1, v2):
    dx = abs(ord(v1[0]) - ord(v2[0])) ** 2
    dy = abs(int(v1[1]) - int(v2[1])) ** 2
    return int((dx + dy) ** 0.5 // 2)


v1, v2 = input().split()
print(kingMoves(v1, v2))

