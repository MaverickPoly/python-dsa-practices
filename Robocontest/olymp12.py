def next_bigger(n):
    digits = list(str(n))
    length = len(digits)

    # finding smaller one
    i = length - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    if i == -1:
        return -1

    # 2017  i = 2
    # 7 <= 2 -> j = 3
    # Finding greater one
    j = length - 1
    while digits[j] <= digits[i]:
        j -= 1

    # Swapping
    digits[i], digits[j] = digits[j], digits[i]

    digits = digits[:i + 1] + sorted(digits[i + 1:])
    return int("".join(digits))


print(next_bigger(12))  # 21
print(next_bigger(512))  # 521
print(next_bigger(2017))  # 2071
print(next_bigger(111))  # -1

