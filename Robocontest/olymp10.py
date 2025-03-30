# 10th Grade  C Task

def equal(lst):
    return all(x == lst[0] for x in lst)


def calc(lst, n):
    count = 0
    while not equal(lst):
        m = max(lst)
        for i in range(n):
            if lst[i] == m:
                continue
            lst[i] += 1
        count += 1
    return count


N = int(input())
l = list(map(int, input().split()))

if equal(l):
    print(0)
else:
    result = calc(l, N)
    print(result)


