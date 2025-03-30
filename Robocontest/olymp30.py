"""
G R O U P S   O F   3 >   C H A R S

Sunatillo o'z o'quvchilarini ICPC musobaqasiga qatnashish uchun tayyorlaydi.
Musobaqa jamoaviy hisoblanadi va har bir jamoada 3 tadan ishtirokchi bo'ladi.
Yaqinda musobaqalar boshlanadi, shuning uchun bolalarni guruhlash kerak.
Musobaqada ahil ishlash juda muhim, shu sababli jamoadagi bolalarning bilimi farqi 1
dan oshmasligi kerak. Aks holda bolalardan kimdir vazifasiz qolib ketadi.
Ustozga nechta jamoani musobaqaga yubora olishini ayting.
"""

n = int(input())
a = list(map(int, input().split()))
a.sort()
result = 0
i = 0
while i + 2 < n:
    if a[i + 2] - a[i] <= 1:
        result += 1
        i += 3
    else:
        i += 1

print(result)


# ------------------------------
# A N O T H E R   C O O L   A L G O R I T H M
def digit_length(x):
    length = 0
    while x > 0:
        x //= 10
        length += 1
    return length


print(digit_length(102))
print(digit_length(1028))
