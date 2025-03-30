"""
Two parallel lines a and b. We have n points in line a and m points in line b.
Task is to find how many triangles can be formed from these points
"""

def count_triangles(n, m):
    # If both lines have fewer than 2 points, no triangles can be formed
    if n < 2 and m < 2:
        return -1

    # Calculate triangles where two points are from line a, one from line b
    case1 = (n * (n - 1)) // 2 * m if n >= 2 else 0

    # Calculate triangles where two points are from line b, one from line a
    case2 = (m * (m - 1)) // 2 * n if m >= 2 else 0

    # Total triangles
    return case1 + case2


# Example input
n = int(input("Enter number of points on line a: "))
m = int(input("Enter number of points on line b: "))

# Output the result
result = count_triangles(n, m)
print(result)
