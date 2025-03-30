# Algorithm to check all pairs of elements in the list sum of which is less than t.

# n - length of array l, t is a boundary number
n, t = tuple(map(int, input().split()))
l = list(map(int, input().split()))
l.sort()
result = 0

left, right = 0, n - 1
while left < right:
    if l[left] + l[right] < t:
        result += (right - left)
        left += 1
    else:
        right -= 1


print(result)
