"""
Current music listening -> X
Using special controls, one can move to k + 1, k - 1, k + 2, k - 2 musics.
Calculate how many times we need to press on the controls to move to Y music.
"""


x = int(input())
y = int(input())

ones = abs(x - y)
twos = ones // 2
ones %= 2
print(ones + twos)




