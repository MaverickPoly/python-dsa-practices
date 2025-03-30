""""


"""


def pop_count(a):
    """Number of ones in binary of a"""
    return bin(a).count("1")


n = int(input())

for i in range(n):
    if i + pop_count(i) == n:
        print(i)
        break
else:
    print(-1)

