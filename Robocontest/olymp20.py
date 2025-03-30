# Teams problem in CodeWars:

"""
build_matches_table(4)
[
  [(1, 2), (3, 4)],  # first round:  1 vs 2, 3 vs 4
  [(1, 3), (2, 4)],  # second round: 1 vs 3, 2 vs 4
  [(1, 4), (2, 3)]   # third round:  1 vs 4, 2 vs 3
]
"""

"""
def build_matches_table(n: int) -> list[list[(int, int)]]:
    teams = list(range(1, n + 1))
    # 1 2 3 4
    rounds = []

    for round_num in range(n - 1):
        round_matches = []
        for i in range(n // 2):
            team1 = teams[i]
            team2 = teams[n - 1 - i]
            round_matches.append((team1, team2))
        rounds.append(round_matches)
        teams = [teams[0]] + [teams[-1]] + teams[1:-1]
    return rounds
"""


# Own implementation
def build_matches_table(n):
    team = list(range(1, n + 1))

    rounds = []

    for round_num in range(n - 1):
        round_matches = []
        for i in range(n // 2):
            team1 = team[i]
            team2 = team[n - i - 1]
            round_matches.append((team1, team2))
        rounds.append(round_matches)
        team = [team[0]] + [team[-1]] + team[1:-1]
    return rounds






print(build_matches_table(4))
print(build_matches_table(6))


