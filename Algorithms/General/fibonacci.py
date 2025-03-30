def get_fibonacci(number):
    if number <= 2: return 1
    return get_fibonacci(number - 1) + get_fibonacci(number - 2)


def generate_fibonacci(number):
    if number <= 0: return []
    result = []
    for i in range(0, number + 1):
        result.append(get_fibonacci(i))
    return result


# 2^n * n -> Time complexity of this function
print(generate_fibonacci(40))

# 1 1 2 3 5 8 13 21 34 55
