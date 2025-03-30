"""
----------- O'yinlar soni ---------
Turnirda
n
n ta jamoa qatnashmoqda. Turnir qoidalari quyidagicha

Agar turnirda qolgan jamoalar soni juft bo'lsa ular 2 ta dan juftliklarga bo'linadi va o'zaro o'yinlarda ishtirok etishadi. G'olib bo'lgan jamoalar keyingi bosqichga yo'l oladi.
Agarda turnirda qolgan jamoalar soni toq bo'lsa, 1 ta jamoa keyingi bosqichga to'g'ridan to'g'ri keyingi bosqichga chiqadi, qolgan jamoalardan esa juftliklarda g'olib bo'lgan jamoalar keyingi bosqichga yo'l oladi.
Shu tariqa 1 ta jamoa qolguncha turnir davom etadi.

Turnir davomida jami nechta o'yin o'tkazilishini aniqlang.

Входные данные:
Kirish faylida
n
n natural son beriladi. Uning qiymati 1 milliarddan oshmaydi.

Выходные данные:
Chiqish faylida jami o'yinlar sonini chop eting.
"""


n = int(input())

count = 0
while n > 1:
    if n % 2 == 0:
        count += n // 2
        n //= 2
    else:
        count += (n - 1) // 2
        n = (n - 1) // 2 + 1

print(count)


