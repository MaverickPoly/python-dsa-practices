"""

"""


def gen_subarray(array):
    subarray = []

    for start in range(len(array)):
        for end in range(start, len(array)):
            subarray.append(array[start:end + 1])
    return subarray




n, k = tuple(map(int, input().split()))
a = list(map(int, input().split()))

sums = []
for arr in gen_subarray(a):
    sums.append(sum(arr))


sums.sort()
print(sums)
print(sums[k - 1])

