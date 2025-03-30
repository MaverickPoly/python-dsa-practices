"""
Enough if dominos are more than 28, else print how many dominos we else need.
"""

n = int(input())   # Number of dominos

if n >= 28:
    print("Enough")
else:
    print(28 - n)

