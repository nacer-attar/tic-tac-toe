import random
from Morpion import cases
def ia_random():
    empty_cells = []
    for l in range(3):
        for c in range(3):
            if cases[l][c] == 0:
                    empty_cells.append((l, c))
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return False
