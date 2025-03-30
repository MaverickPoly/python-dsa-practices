arr = [int(input()) for i in range(10)]


d = {i: 0 for i in range(42)}
for i in arr:
    d[i % 42] += 1


num = 0
for i in range(42):
    if d[i] > 0:
        num += 1

print(num)
