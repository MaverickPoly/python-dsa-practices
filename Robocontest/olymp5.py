s1 = input()
s2 = input()
unli = ['a', 'e', 'i', 'o', 'u', 'y']
result = 0


for (char1, char2) in zip(s1, s2):
    if char1 == char2:
        continue
    print(char1, end="   ")
    print(char2)
    if (char1 in unli and not char2 in unli) or (char2 in unli and not char1 in unli):
        result += 1

print(result)
