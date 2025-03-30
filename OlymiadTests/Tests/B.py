a, b, c = map(int, input().split())
x, y = map(int, input().split())

v1, v2 = min(a, x), min(b, y)
rem_x, rem_y = x - v1, y - v2
m = min(min(rem_y, rem_x), c)
print(v1 + v2 + m)

