from functools import reduce


def gen(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i < num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    result = []
    for i in range(1, n + 1):
        if is_prime(i):
            result.append(i)
    print(result)
    return result


n = int(input())
mult = reduce(lambda x, y: x * y, gen(n))

print(mult)
count = 0
while mult % 10 == 0:
    count += 1
    mult //= 10

print(count)
