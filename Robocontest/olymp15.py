# Grade 11 B Problem

st = input()

rev = ""
for char in st:
    if char == "d":
        rev = "b" + rev
    elif char == "b":
        rev = "d" + rev
    else:
        rev = char + rev

if "r" in rev or "R" in rev:
    print("Not readable!")
else:
    print(rev)

