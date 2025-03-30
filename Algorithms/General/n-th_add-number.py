def first_approach(n):
    result = 1
    for i in range(n * 2):
        if i % 2 == 0:
            continue
        result = i
    return result


def second_approach(n):
    return list(filter(lambda x: x % 2 != 0, [i for i in range(n * 2)]))[-1]


print(first_approach(3))
print(second_approach(3))

print(first_approach(6))
print(second_approach(6))

print(first_approach(7))
print(second_approach(7))

