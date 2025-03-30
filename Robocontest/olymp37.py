"""
Very powerful algorithm!!

Converts number from binary to decimal if it is binary, else forms one below binary from it and then
performs the same thing.

For example:
10 -> 2
20 (11) -> 3

"""

n = int(input())
n_str = str(n)
binary = ""
found_invalid = False

for digit in n_str:
    if not found_invalid and digit in "01":
        binary += digit
    else:
        found_invalid = True
        binary += "1"

print(binary)
print(int(str(binary), 2))

