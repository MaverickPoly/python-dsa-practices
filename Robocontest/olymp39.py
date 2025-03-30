v1, v2 = input().split()
dx = abs(ord(v1[0]) - ord(v2[0])) ** 2
dy = abs(int(v1[1]) - int(v2[1])) ** 2

# (x1 - x2)**2 + (y1 - y2)**2

print(int(dy + dx) ** 0.5 // 2)
