a, b, c, d = map(int, input().split())

l = [a, b, c]
v = sorted(l)[:2]
if sum(v) / 60 < d:
    print("YES")
else:
    print("NO")
