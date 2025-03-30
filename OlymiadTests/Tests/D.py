n, m = map(int, input().split())  # questions, students
k = list(map(int, input().split()))

readiness = [0] * m
min_raised = float("inf")

for question in range(n):
    hands_raised = 0
    for student in range(m):
        if readiness[student] == 0:
            hands_raised += 1
        else:
            readiness[student] -= 1

    if hands_raised == 0:
        print(0)
        exit()

    min_raised = min(min_raised, hands_raised)
    readiness[question % m] = k[question % m]

print(min_raised)

