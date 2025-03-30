# def increment(array, x, y):
#     for i in range(x):
#         array[i] += y
#     return array
#
#
# def decrement(array, x, y):
#     for i in range(x):
#         array[i] -= y
#     return array[::-1]


n, q = tuple(map(int, input().split()))

array = [0 for _ in range(n)]

for t, x, y in [[l for l in list(map(int, input().split()))] for _ in range(q)]:
    if t == 1:
        # array = increment(array, x, y)
        for i in range(x):
            array[i] += y
    else:
        # array = decrement(array[::-1], x, y)
        for i in range(x):
            array[len(array) - i - 1] -= y

print(max([abs(i) for i in array]))
