def is_pal(st):
    return st == "".join(list(reversed(st)))


s = input()

if is_pal(s):
    print(s)
else:
    for i in range(int(s) - 1, 1, -1):
        if is_pal(str(i)):
            print(i)
            break
