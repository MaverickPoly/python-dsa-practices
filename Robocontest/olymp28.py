"""
Sizga 2 ta butun sonlar
n va m beriladi. Siz esa quyidagi ikki summalar orasidagi farqni topishingiz kerak bo'ladi.

 1 dan n gacha bo'lgan sonlardan m ga bo'linmaydiganlari yig'indisi
1 dan
n
n gacha bo'lgan sonlardan
m
m ga bo'linadiganlar yig'indisi
1 va 2-yig'indilar farqini toping.

Ikkalar holda ham 1 va n hisobga olinadi.

Входные данные:
Kirish faylida birinchi qatorda 2 ta butun son n va m beriladi.
1 ≤ n, m ≤ 10^9

Выходные данные:
Chiqish faylida ikki yig'indilar orasidagi farq ya'ni modulini toping.
"""

n, m = map(int, input().split())

k = n // m
total = (n * (n + 1)) // 2
s1 = m * (k * (k + 1)) // 2
s2 = total - s1
print(abs(s1 - s2))
