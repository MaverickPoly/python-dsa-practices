import math
chars = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8
}

a = input()
b = input()

res1, res2 = math.ceil(abs(chars[a[0]] - chars[b[0]]) / 2), math.ceil(abs(int(a[1]) - int(b[1])) / 2)
print(max(res1, res2))
