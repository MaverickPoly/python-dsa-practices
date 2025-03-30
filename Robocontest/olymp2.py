n = int(input())
weights = list(map(int, input().split()))
weights.sort(reverse=True)
an = 0
bo = 0
for i, weight in enumerate(weights):
    if i % 2 == 0:
        an += weight
    else:
        bo += weight

print(an)
print(bo)

if an > bo:
    print("Anvar")
elif bo > an:
    print("Bobur")
else:
    print("Durrang")
