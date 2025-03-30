"""
Number of seconds it takes to type all the word. One char -> One second
CapsLock = 2 seconds
Shift = 1 second
"""


n = int(input())
st = input().split()

result = 0
for word in st:
    uppercase = len([char for char in word if char.isupper()])
    print(uppercase)
    lowercase = len(word) - uppercase
    print(lowercase)
    print("------")
    shift_time = 2 * uppercase + lowercase + 1
    cap_time = 2 + uppercase + lowercase + 1
    result += min(cap_time, shift_time)

print(result - 1)

