"""
All the boys have A[i] amount of apples. How many times boys have to
climb tree, if they can take one apple for each of their friends.
"""


n = int(input())
a = list(map(int, input().split()))

count = 0

while not all(i == a[0] for i in a):
    m = max(a)
    index = a.index(m)
    print(a)
    for i in range(n):
        if i != index:
            a[i] += 1
    count += 1


print(count)

