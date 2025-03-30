"""
Senior should make more problems than workers.
a[j] >= a[i]
"""

n = int(input())
a = list(map(int, input().split()))


result = []


for index, j in enumerate(a):
    s = 0
    for ind, i in enumerate(a):
        if index == ind:
            continue
        if j < i:
            s += i - j
    result.append(str(s))


print(" ".join(result))


