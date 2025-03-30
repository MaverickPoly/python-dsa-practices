import heapq

n, k = map(int, input().split())
s = list(map(int, input().split()))


heap = []
for satisfaction in s:
    heapq.heappush(heap, -satisfaction)

total = 0

for i in range(k):
    if heap:
        max_sat = -heapq.heappop(heap)
        total += max_sat
        if max_sat > 0:
            heapq.heappush(heap, -(max_sat - 1))

print(total)

