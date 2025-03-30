# CodeForces problem

price = int(input())

max_fives = price // 5
remainder = price % 5

while remainder % 2 != 0:
    max_fives -= 1
    remainder = price - (max_fives * 5)

result = max_fives + remainder // 2
print(result)


# ---------------------------
# Reverse a string


def reverse(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s


# print(reverse([3, 4, 5, 7, 4]))
