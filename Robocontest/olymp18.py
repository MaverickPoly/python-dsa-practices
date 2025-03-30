
import math

# Memoization dictionary to store the minimum number of 1's required for each number
memo = {1: 1}


def min_ones(n):
    if n in memo:
        return memo[n]

    min_count = n  # The worst case is using `1` added `n` times (n 1's).

    # Try to divide `n` into factors a * b = n
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            a, b = i, n // i
            # Calculate the number of 1's if we split `n` as `a * b`
            min_count = min(min_count, min_ones(a) + min_ones(b))

    # Store the result in memo dictionary
    memo[n] = min_count
    return min_count


# Example usage
print(min_ones(3))  # Expected output: 6
# print(min_ones(11))  # Expected output: 8
