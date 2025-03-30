# Prime numbers associated with
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


def find_smallest_non_divisible(n):
    primes = first_n_primes(n)
    candidate = 2
    while True:
        if all(candidate % prime != 0 for prime in primes):
            return candidate
        candidate += 1


N = int(input())
result = find_smallest_non_divisible(N)
print(result)

