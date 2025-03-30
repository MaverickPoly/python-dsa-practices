"""
In this problem, we need to find Nth + 1 'tub' number.
"""


def is_tub(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def gen_tub(num):
    count = 0
    result = 1
    while count != num:
        result += 1
        if is_tub(result):
            count += 1
    return result


n = int(input())
print(gen_tub(n + 1))


