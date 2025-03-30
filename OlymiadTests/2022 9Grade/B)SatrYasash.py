"""
Construct a new string given a list of amounts of each letter. 
Two same letters cannot be near each other!

E.G: 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 -> axyza
"""

import heapq


def construct_string(frequencies):
    pq = []
    for i, amount in enumerate(frequencies):
        if amount > 0:
            heapq.heappush(pq, (-amount, chr(ord("a") + i)))

    result = []
    prev_char, prev_count = None, 0
    while pq:
        count, char = heapq.heappop(pq)
        result.append(char)
        if prev_count < 0:
            heapq.heappush(pq, (prev_count, prev_char))
        prev_char, prev_count = char, count + 1
    return "".join(result)


frequencies = list(map(int, input().split()))
print(construct_string(frequencies))

