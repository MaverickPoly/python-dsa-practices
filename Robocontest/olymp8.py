def get_subarr(array):
    subarray = []
    for start in range(len(array)):
        for end in range(start, len(array)):
            subarray.append(array[start:end + 1])
    return subarray


n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
sub_sums = []
for sub_arr in get_subarr(arr):
    sub_sums.append(sum(sub_arr))
print(sub_sums)
sub_sums.sort()
print(sub_sums)
print(sub_sums[k - 1])
