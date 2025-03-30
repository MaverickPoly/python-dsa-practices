"""
Number of steps needed to build palindrome string out of simple string.

For example:
aaabbbbcb -> 7
abcb -> 3
ba -> 1

kkyii -> 5 -> kiyik
nano -> 3 -> nan

"""

from collections import Counter

s = input()

counter = Counter(s)
has_odd = False
length = 0

for count in counter.values():
    length += (count // 2) * 2
    if count % 2 == 1:
        has_odd = True

if has_odd:
    length += 1

print(length)

