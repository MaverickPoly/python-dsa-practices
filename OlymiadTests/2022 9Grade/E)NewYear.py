"""
Qorbobo va Qorqiz ta yangi yil sovg‘asini bolalarga yetkazishi kerak. -sovg‘ani Qorqiz
daqiqada tayyorlaydi, Qorbobo tayyor bo’lgan sovg’ani egasiga yetkazib berish uchun
daqiqa vaqt saraydi. Qorboboning xaltasiga bittadan ortiq sovg‘a sig‘maydi. Qorqiz ham
bir vaqtni o‘zida bitta sovg‘ani tayyorlay oladi. Qorbobo va Qorqiz eng minimal qancha
daqiqada barcha sovg‘alarni yetkaza olishadi?
"""

def minimal_delivery_time(n, a, b):
    qorqiz_time = 0
    prev_total = 0

    for i in range(n):
        qorqiz_time += a[i]
        prev_total = max(prev_total, qorqiz_time) + b[i]
    return prev_total


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(minimal_delivery_time(n, a, b))
