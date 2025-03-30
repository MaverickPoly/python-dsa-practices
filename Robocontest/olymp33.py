"""
# Draws the helicopter parking area sign

n = int(input())
mid = n // 2
for i in range(n):
    print("H", end="")
    if i == mid:
        print("H" * (n - 2), end="")
    else:
        print(" " * (n - 2), end="")
    print("H", end="")
    print()
"""

"""
Sardor xonasini tozalamoqchi. U bo‘sh joyning katta qismini o‘yinchoqlar, poyabzallar, gugurtlarning bo‘sh 
qutilari egallaganini payqab qoldi... Bola bir nechta qutilarni boshqalarning ichiga qo‘yishga qaror qildi 
va shu tariqa ko‘p joyni tejashga qaror qildi. Qutilar juda o'ziga xos shaklga ega - har bir qutiga faqat bitta 
kichikroq quti qo'yilishi mumkin. Albatta, bu kichikroq quti ichida boshqa, hatto undan ham kichikroq quti bo'lishi 
mumkin. Sardor xonani tozalagandan keyin u yerda qancha quti ko'rinishini ayting.


Basically, after placing smaller boxes into larger ones, how many boxes left we will have.

    Below is amazing algorithm for this task!!!
"""

n = int(input())
a = sorted(map(int, input().split()))
print(a)

visible_boxes = n
start = 0

for end in range(n):
    print(f"END: {end}", end="\t")
    if a[start] < a[end]:
        print("YES")
        visible_boxes -= 1
        start += 1

print(visible_boxes)

