t = int(input())  # Number of test cases

res = []
for i in range(t):
    st = input()
    if len(st) == 1:
        res.append(f"{chr(ord(st) + 1)}{st}")
        continue
    j = 0
    current = ""
    left = 1
    while j < len(st):
        current += st[j]
        if left and st[j] == st[j + 1]:
            current += chr(ord(st[j]) + 1)
            left -= 1
        j += 1

    res.append(current)

print("\n".join(res))