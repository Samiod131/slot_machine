import numpy as np
import random
from pprint import pprint

# Setting formats for reelsets and paytables.

reelset = [
    [
        "sym2",
        "sym7",
        "sym7",
        "sym1",
        "sym1",
        "sym5",
        "sym1",
        "sym4",
        "sym5",
        "sym3",
        "sym2",
        "sym3",
        "sym8",
        "sym4",
        "sym5",
        "sym2",
        "sym8",
        "sym5",
        "sym7",
        "sym2",
    ],
    [
        "sym1",
        "sym6",
        "sym7",
        "sym6",
        "sym5",
        "sym5",
        "sym8",
        "sym5",
        "sym5",
        "sym4",
        "sym7",
        "sym2",
        "sym5",
        "sym7",
        "sym1",
        "sym5",
        "sym6",
        "sym8",
        "sym7",
        "sym6",
        "sym3",
        "sym3",
        "sym6",
        "sym7",
        "sym3",
    ],
    [
        "sym5",
        "sym2",
        "sym7",
        "sym8",
        "sym3",
        "sym2",
        "sym6",
        "sym2",
        "sym2",
        "sym5",
        "sym3",
        "sym5",
        "sym1",
        "sym6",
        "sym3",
        "sym2",
        "sym4",
        "sym1",
        "sym6",
        "sym8",
        "sym6",
        "sym3",
        "sym4",
        "sym4",
        "sym8",
        "sym1",
        "sym7",
        "sym6",
        "sym1",
        "sym6",
    ],
    [
        "sym2",
        "sym6",
        "sym3",
        "sym6",
        "sym8",
        "sym8",
        "sym3",
        "sym6",
        "sym8",
        "sym1",
        "sym5",
        "sym1",
        "sym6",
        "sym3",
        "sym6",
        "sym7",
        "sym2",
        "sym5",
        "sym3",
        "sym6",
        "sym8",
        "sym4",
        "sym1",
        "sym5",
        "sym7",
    ],
    [
        "sym7",
        "sym8",
        "sym2",
        "sym3",
        "sym4",
        "sym1",
        "sym3",
        "sym2",
        "sym2",
        "sym4",
        "sym4",
        "sym2",
        "sym6",
        "sym4",
        "sym1",
        "sym6",
        "sym1",
        "sym6",
        "sym4",
        "sym8",
    ],
]


paytable = {
    "sym1": {3: 1, 4: 2, 5: 3},
    "sym2": {3: 1, 4: 2, 5: 3},
    "sym3": {3: 1, 4: 2, 5: 5},
    "sym4": {3: 2, 4: 5, 5: 10},
    "sym5": {3: 5, 4: 10, 5: 15},
    "sym6": {3: 5, 4: 10, 5: 15},
    "sym7": {3: 5, 4: 10, 5: 20},
    "sym8": {3: 10, 4: 20, 5: 50},
}


def get_random_reel_positions(reelset):
    return [random.randint(0, len(reel) - 1) for reel in reelset]


def get_screen_matrix(reelset, positions, height=3):
    columns = []
    for i, reel in enumerate(reelset):
        start_pos = positions[i] - (height // 2) + (height + 1) % 2
        end_pos = positions[i] + (height // 2)
        if end_pos >= len(reel):
            end_pos -= len(reel)
        if start_pos < 0:
            start_pos += len(reel)

        if start_pos <= end_pos:
            columns.append(reel[start_pos : end_pos + 1])
        else:
            columns.append(reel[start_pos:] + reel[: end_pos + 1])
    return columns

def get_ways(screen_matrix):
    


def get_wins(screen_matrix):
    win_pos, symbols = get_ways(screen_matrix)
    earnings = get_earnings(win_pos, symbols)

    return earnings


# positions = get_random_reel_positions(reelset=reelset)
# print(positions)

pprint(reelset)
positions = [-1, -1, -1, -1, -1]
print(get_screen_matrix(reelset, positions))
