def get_all_subarray(array):
    subarray = []

    for start in range(len(array)):
        for end in range(start, len(array)):
            subarray.append(array[start:end + 1])
    return subarray


# print(get_all_subarray([1, 2, 3]))


# Max Sum of subarray
def max_sequence(arr):
    if not arr:
        return 0

    current_sum = arr[0]
    max_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(current_sum, max_sum)
    return max_sum if max_sum > 0 else 0


print(max_sequence([1, 2, 3, 5]))


