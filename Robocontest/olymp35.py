"""
Sizga 2 ta satr berilgan. Siz bu ikki satrlar ustida quyidagi amallarni bajarish orqali bir-biriga tenglashingiz kerak:

istalgan satrni tanlang va bu satrning bitta belgisini o'chirib yuboring
istalgan satrni tanlang va bu satrning 2 ta belgisi joylashuvini o'zgartiring
Yuqorida berilgan topshiriqni bajargandan so'ng, mumkin bo'lgan eng uzun satr uzunligini chop eting.

Input:
s -> First string, t -> second string


Bitta yagona qatorda s ning maximum uzunligini chop eting.

Examples:
    1.
dbcd
bdaacd
Output: 4
    2.
cd
bb
Output: 0
    3.
ddcacdb
ddccca
Output: 5
"""

s, t = input(), input()  # input().strip()

result = 0
for i in range(97, 123):
    result += min(s.count(chr(i)), t.count(chr(i)))

print(result)

