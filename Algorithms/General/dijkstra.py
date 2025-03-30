import math


# Get all points that are connected to the current point
def get_link_v(v, D):
	for i, weight in enumerate(D[v]):
		if weight > 0:
			yield i



# Find the minimum distance in the graph's point
def arg_min(T, S):
	amin = -1  # Index of Min
	m = max(T)
	for i, t in enumerate(T):
		if t < m and i not in S:
			m = t
			amin = i

	return amin


# Simulation of the graph
D = (
		(0, 3, 1, 3, 0, 0),
		(3, 0, 4, 0, 0, 0),
		(1, 4, 0, 0, 7, 5),
		(3, 0, 0, 0, 0, 2),
		(0, 0, 7, 0, 0, 4),
		(0, 0, 5, 2, 4, 0),
	)

N = len(D)  # Length of the graph
T = [math.inf] * N  # Result array with lengths

v = 0  # Index of Current point in the graph
S = {v}  # Set of all visited points in Graph
T[v] = 0  # Current point in the graph

while v != -1:
	for j in get_link_v(v, D):
		if j not in S:
			w = T[v] + D[v][j]
			if w < T[j]:
				T[j] = w

	v = arg_min(T, S)
	if v > 0:
		S.add(v)

print(T)
