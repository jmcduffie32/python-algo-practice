import math
import random

luoshu = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]


def verfiy_square(square):
    sums = []
    row_sums = [sum(square[i]) for i in range(len(square))]
    sums.append(row_sums)
    col_sums = [sum([row[i] for row in square]) for i in range(len(square))]
    sums.append(col_sums)
    main_diag = sum([square[i][i] for i in range(len(square))])
    sums.append([main_diag])
    anti_diag = sum([square[i][len(square) - 1 - i] for i in range(len(square))])
    sums.append([anti_diag])
    flattened = [el for arr in sums for el in arr]
    return len(list(set(flattened))) == 1


def print_square(square):
    labels = ["[" + str(x) + "]" for x in range(len(square))]
    format_row = "{:>6}" * (len(labels) + 1)
    print(format_row.format("", *labels))
    for label, row in zip(labels, square):
        print(format_row.format(label, *row))


def rule_1(x, n, up_right):
    return (x + ((-1) ** up_right) * n) % n**2


def rule_2(x, n, up_left):
    return (x + ((-1) ** up_left)) % n**2


def rule_3(x, n, up_left):
    return (x + ((-1) ** up_left * (-n + 1))) % n**2


def fill_square(square, entry_i, entry_j, how_full):
    while sum(math.isnan(i) for row in square for i in row) > how_full:
        where_we_can_go = []

        if entry_i < (n - 1) and entry_j < (n - 1):
            where_we_can_go.append("down_right")
        if entry_i < (n - 1) and entry_j > 0:
            where_we_can_go.append("down_left")
        if entry_i > 0 and entry_j < (n - 1):
            where_we_can_go.append("up_right")
        if entry_i > 0 and entry_j > 0:
            where_we_can_go.append("up_left")

        where_to_go = random.choice(where_we_can_go)
        if where_to_go == "up_right":
            new_entry_i = entry_i - 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = rule_1(square[entry_i][entry_j], n, True)

        if where_to_go == "down_left":
            new_entry_i = entry_i + 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = rule_1(
                square[entry_i][entry_j], n, False
            )

        if where_to_go == "up_left" and (entry_i + entry_j) != n:
            new_entry_i = entry_i - 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = rule_2(square[entry_i][entry_j], n, True)

        if where_to_go == "down_right" and (entry_i + entry_j) != (n - 2):
            new_entry_i = entry_i + 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = rule_2(
                square[entry_i][entry_j], n, False
            )

        if where_to_go == "up_left" and (entry_i + entry_j) == n:
            new_entry_i = entry_i - 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = rule_3(square[entry_i][entry_j], n, True)

        if where_to_go == "down_right" and (entry_i + entry_j) == n - 2:
            new_entry_i = entry_i + 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = rule_3(
                square[entry_i][entry_j], n, False
            )

        entry_i = new_entry_i
        entry_j = new_entry_j

    return square


n = 11
square = [[float("nan") for i in range(n)] for j in range(n)]
center_i = math.floor(n / 2)
center_j = math.floor(n / 2)

square[center_i][center_j] = int((n**2 + 1) / 2)
square[center_i + 1][center_j] = 1
square[center_i - 1][center_j] = n**2
square[center_i][center_j + 1] = n**2 + 1 - n
square[center_i][center_j - 1] = n


entry_i = math.floor(n / 2)
entry_j = math.floor(n / 2)

# fill first set of diagonals
square = fill_square(square, entry_i, entry_j, n**2 / 2 - 4)

# fill rest
entry_i = math.floor(n / 2) + 1
square = fill_square(square, entry_i, entry_j, 0)

# replace 0 with n**2
square = [[n**2 if x == 0 else x for x in row] for row in square]

print_square(square)
print("Is magic?: " + str(verfiy_square(square)))
