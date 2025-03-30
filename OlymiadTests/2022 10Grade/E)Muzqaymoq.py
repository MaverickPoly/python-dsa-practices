"""
N -> number of ice-cream types
c[i] -> price of i-type ice-cream

Q -> number of visitors to the store
a[k] -> number of money k-th visitor has

Output:
- Maximum amount of money a[k] visitor can spend
- Number of ice-creams of c[i] type that visitor should buy
"""


n = int(input())
c = list(map(int, input().split()))
Q = int(input())
a = list(map(int, input().split()))


sorted_prices = sorted(enumerate(c), key=lambda x: x[1], reverse=True)

for visitor in a:
    total_spent = 0
    types_count = [0] * n
    for i, price in sorted_prices:
        if total_spent + price <= visitor:
            max_count = (visitor - total_spent) // price
            types_count[i] = max_count
            total_spent += max_count * price

    print(total_spent)
    print(types_count)

"""
for i, visitor in enumerate(a):
    copy = c[:]
    amount = 0
    result = [0] * n
    for _ in range(len(c)):
        m = max(copy)
        if m + amount <= visitor:
            index = copy.index(m)
            amount += m
            result[index + 1] += 1
        print(copy)
        copy.remove(m)

    print(amount)
    print(" ".join(list(map(str, result))))
"""



