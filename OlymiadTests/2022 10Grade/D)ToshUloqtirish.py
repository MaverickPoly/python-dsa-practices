"""
O - starting position
X -> target position

a, b -> parameters

Throw length = a * b
l1 <= a <+ r1
l2 <= b <= r2
"""


def calc(a_pos, b_pos, x):
    for a_p in a_pos:
        for b_p in b_pos:
            if a_p * b_p == abs(x):
                return a_p, b_p
    return "Impossible"


x, l1, r1, l2, r2 = tuple(map(int, input().split()))

direction = "Left" if x < 0 else "Right"
a_pos = [i for i in range(l1, r1 + 1)]
b_pos = [i for i in range(l2, r2 + 1)]

res = calc(a_pos, b_pos, x)
if res == "Impossible":
    print("Impossible")
else:
    print(direction)
    print(res[0], res[1])



