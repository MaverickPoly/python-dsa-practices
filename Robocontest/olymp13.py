def round_to_next_n(number, n):

    return ((number + n - 1) // n) * n


print(round_to_next_n(4, 5))  # 5
print(round_to_next_n(15, 4))  # 16
print(round_to_next_n(11, 3))  # 12
print(round_to_next_n(5, 2))  # 6
print(round_to_next_n(40, 7))  # 42



# -------------- Counter function ---------------
"""
from collections import Counter


res = Counter("hello")
print(res.values())
print(res.keys())
frequency = max(res.values())
print(frequency)
ind = list(res.values()).index(frequency)
print(ind)
char = list(res.keys())[ind]
print(char)

"""
