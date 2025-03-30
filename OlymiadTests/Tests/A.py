a, b, c, d = map(int, input().split())
l = [a, b, c]
m = max(l)
l.remove(m)
s = sum(l)

if s / 60 > d:
    print("NO")
else:
    print("YES")

