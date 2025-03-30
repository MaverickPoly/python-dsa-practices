n, k = map(int, input().split())
a = list(map(int, input().split()))

m = max(a)
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if k * a[j] * a[i] > m:
            count += 1


print(count)

