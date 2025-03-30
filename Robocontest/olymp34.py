"""
Qurbaqa 1 dan boshlab raqamlangan cheksiz toshlarning
a
a raqamli toshida o'tiribdi. Qurbaqa bir sakrashda agar
x
x raqamli toshda turgan bo'lgan bo'lsa
2
×
x
2×x yoki
2
×
x
+
1
2×x+1 toshga sakrashi mumkin. Qurbaqa b raqamli toshga bora oladimi?

Examples:
    Input:
        2
        2 12
        3 12
    Output:
        No
        Yes
"""


def can_reach(tests):
    results = []
    for a, b in tests:
        while b > a:
            if b % 2 == 0:
                b //= 2
            else:
                b = (b - 1) // 2
        if b == a:
            results.append("Yes")
        else:
            results.append("No")
    return results


t = int(input())
test_cases = [map(int, input().split()) for _ in range(t)]
print("\n".join(can_reach(test_cases)))

