import heapq

n, k = map(int, input().split())
s = list(map(int, input().split()))

heap = []
for satisfaction in s:
    heapq.heappush(heap, -satisfaction)

total = 0
for _ in range(k):
    max_satisfaction = -heapq.heappop(heap)
    total += max_satisfaction
    if max_satisfaction > 0:
        heapq.heappush(heap, -(max_satisfaction - 1))

print(total)


