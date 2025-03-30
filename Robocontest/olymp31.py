def digit_length(x):
    length = 0
    while x > 0:
        x //= 10
        length += 1
    return length


n = int(input())

v1 = sorted(map(int, input().split()))
v2 = sorted(map(int, input().split()), reverse=True)
print(v1, v2)

# 3
# 5 2 30
# 13 9 7
result = 0
for (a, b) in zip(v1, v2):
    length = digit_length(b)
    # 38  2
    # 2 * (10) + 7 = 27
    result += a * (10 ** length) + b

print(result)
