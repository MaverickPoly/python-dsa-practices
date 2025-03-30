"""
Make string A equal to string B.
Unli -> Unli, and Undosh -> Undosh => Free
Others => 1
"""

unli = ["a", "e", "i", "o", "u", "y"]

s1 = input()
s2 = input()

price = 0
for char1, char2 in zip(s1, s2):
    if (char1 in unli and char2 not in unli) or (char2 in unli and char1 not in unli):
        price += 1


print(price)

