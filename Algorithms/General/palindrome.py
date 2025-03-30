def reverse(text):
    result = ""
    for char in text:
        result = char + result
    return result


def check_palindrome(text):
    reversed_string = reverse(text)
    return reversed_string == text


print(check_palindrome("abba"))
print(check_palindrome("hello"))
print(check_palindrome("world"))
print(check_palindrome("bannab"))




