"""
The program that checks if the provided coordinates form a straight line or not.
First list is coordinates of x
Second list is coordinates of y
"""

x = list(map(int, input().split()))
y = list(map(int, input().split()))

dy = y[1] - y[0]
dx = x[1] - x[0]
print(dx, dy)

for i in range(2, len(x)):
    if (y[i] - y[i - 1]) * dx != (x[i] - x[i - 1]) * dy:
        print((y[i - 1] + y[i]) * dx)
        print((x[i] + x[i - 1]) * dy)
        print("YO'Q")
        break
else:
    print("HA")

