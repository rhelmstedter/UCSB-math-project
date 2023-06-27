"""
How many combinations of TDs (7 points) and FGs (3 points) are there to make 83 points?
Of the possible combinations, which results in the most pushups?
"""
from itertools import accumulate

MAX_TDS = 11
TOTAL_SCORE = 83

combs = []
for tds in range(MAX_TDS, 0, -3):
    td_points = tds * 7
    remaing_points = TOTAL_SCORE - td_points
    if remaing_points % 3 == 0:
        fgs = remaing_points // 3
        combs.append((tds, fgs))
    else:
        continue

print("There are four possible ways to score 83 points with TDs and FGs.")
print("TDs | FGs | Total Pushups")
print("-------------------------")
for tds, fgs in combs:
    points_added = [7] * tds + [3] * fgs
    total_pushups = sum(accumulate(points_added))
    print(f"{tds:>3} | {fgs:>3} | {total_pushups:>13}")
