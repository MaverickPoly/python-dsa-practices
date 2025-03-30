n, k = map(int, input().split())
a = list(map(int, input().split()))

pairs = []
count = 0
for i in range(n):
    for j in range(i + 1, n):
        m = max(a[i:j + 1])
        if a[i] * a[j] * k > m:
            pairs.append((i, j))
            count += 1

print(count)
