"""
Binary String super problem.
"""


def find_smallest_integer(s):
    seen_values = set()
    max_bits = 20

    for start in range(len(s)):
        current_value = 0
        for length in range(max_bits):
            if start + length >= len(s):
                break
            current_value = (current_value << 1) | int(s[start + length])
            seen_values.add(current_value)

    smallest_missing = 1
    while smallest_missing in seen_values:
        smallest_missing += 1

    return smallest_missing


print(find_smallest_integer("100110"))
print(find_smallest_integer("1111"))
