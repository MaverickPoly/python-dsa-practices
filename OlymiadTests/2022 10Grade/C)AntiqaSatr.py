"""
we have a long string:
110100100010000...
We need to find K's element of it.
"""




# Not the fastest solution ever! Need to modify it!
while True:
    k = int(input())

    st = ""
    for i in range(k // 2 + 1):
        st += "1" + "0" * i


    print(st)
    print(st[k - 1], end="\n\n")

