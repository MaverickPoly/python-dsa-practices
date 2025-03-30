a, b, c = map(int, input().split())
x, y = map(int, input().split())

v1 = min(a, x)
v2 = min(b, y)
rem_x, rem_y = x - v1, y - v2
print(rem_x, rem_y)
if rem_x and rem_y and c:
    r = min(min(rem_x, rem_y), c)
    print(r + v1 + v2)
else:
    print(v1 + v2)
