def get_factorial(number):
    if number <= 1:
        return 1
    return number * get_factorial(number - 1)


def generate_factorial(number):
    if number <= 0: return -1
    result = []
    for i in range(1, number + 1):
        result.append(get_factorial(i))
    return result


print(generate_factorial(10))
print(generate_factorial(5))
print(get_factorial(5))
print(generate_factorial(-5))


