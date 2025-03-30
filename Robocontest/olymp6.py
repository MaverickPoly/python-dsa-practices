import math

n = int(input())
st = input()
first = st.index(".")
temp = st[first:]
last = temp.index("#")
print(math.ceil((last - first) / 2) + 1)

"""
##...##.

first = 2
temp = ...##.
last = 3
print(math.ceil((3 - 2) / 2) + 1 + len(st) - len(temp))

"""

