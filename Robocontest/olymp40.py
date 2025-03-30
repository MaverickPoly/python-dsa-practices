s = input()
result = ""

# utils
numbers = ""
currentSum = 0

for char in s:
    if char.isdigit():
        numbers += char
    else:
        if numbers:
            currentSum += int(numbers)
            result += str(currentSum)
            numbers = ""
        result += char

if numbers:
    currentSum += int(numbers)
    result += str(currentSum)

print(result)

