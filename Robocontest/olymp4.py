def is_power_of_three(n):
    if n <= 2:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1



ar = list(map(int, input().split()))
for el in ar:
    if not is_power_of_three(el):
        print(el)
        break


# TEST CUSTOM FOR EXERCISE

def is_power_of_four(n):
    if n < 4:
        return False
    while n % 4 == 0:
        n //= 4
    return n == 1


print(is_power_of_four(4))
print(is_power_of_four(5))
print(is_power_of_four(8))
print(is_power_of_four(16))

