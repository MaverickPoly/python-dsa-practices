"""
We need to find the length of the array when all elements will be added until they are all >= 4.
Example:
    7 4
    1 2 3 4 3 1 1
    6 4 5
Output:
    3

"""

n, w = map(int, input().split())
a = list(map(int, input().split()))

res = 0
current = 0
for i in a:
    current += i
    if current >= w:
        res += 1
        current = 0


print(res)
