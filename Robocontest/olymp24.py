"""
Problem:
We need to calculate the total number of trailing zeros of the factorial of n.

Traditional way is very slow and causes error in very big numbers.
So this is much better algorithm:
"""


def traditional(n):
    def factorial(num):
        if num <= 1:
            return 1
        return num * factorial(num - 1)

    answer = factorial(n)
    count = 0
    while answer % 10 == 0 and answer != 0:
        count += 1
        answer //= 10
    return count


print(traditional(30))  # 7


# Better version
def better_algorithm(n):
    count = 0
    power_of_five = 5
    while n >= power_of_five:
        count += n // power_of_five
        power_of_five *= 5
    return count


print(better_algorithm(30))  # 7














