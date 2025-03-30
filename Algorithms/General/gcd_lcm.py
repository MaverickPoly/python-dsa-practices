import math


# ---------- GCD -----------
def math_gcd(*args):
    return math.gcd(*args)


def custom_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print(custom_gcd(17, 34))


# ------------- LCM ----------
def math_lcm(*args):
    return math.lcm(*args)


def custom_lcm(a, b):
    return abs(a * b) // custom_gcd(a, b)


print(custom_lcm(3, 7))



