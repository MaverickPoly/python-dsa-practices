# Direction Reduction problem -> CodeWars

def dir_reduce(arr):
    opposites = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"
    }

    stack = []
    for direction in arr:
        if stack and stack[-1] == opposites[direction]:
            stack.pop()
        else:
            stack.append(direction)
    return stack


print(dir_reduce(["NORTH", "SOUTH", "EAST", "WEST", "SOUTH"]))


# U S E F U L   INT()   F U N C T I O N


def binaryToDecimal(n):
    return int(n, 2)  # n must be a string, not integer


print(binaryToDecimal("1010"))
print(binaryToDecimal("1011"))


# ord("a") => 97, so we need to subtract 96 from it to get the first digit in the alphabet

