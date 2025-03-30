target_positions = {
    "A": (0, 0), "B": (0, 1), "C": (0, 2), "D": (0, 3),
    "E": (1, 0), "F": (1, 1), "G": (1, 2), "H": (1, 3),
    "I": (2, 0), "J": (2, 1), "K": (2, 2), "L": (2, 3),
    "M": (3, 0), "N": (3, 1), "O": (3, 2), ".": (3, 3),
}


def calculate_min_energy(grid):
    energy = 0
    for i in range(4):
        for j in range(4):
            letter = grid[i][j]
            target_x, target_y = target_positions[letter]

            energy += abs(i - target_x) + abs(j - target_y)
    return energy


initial_grid = [input().strip() for _ in range(4)]
min_energy = calculate_min_energy(initial_grid)
print(min_energy)

