import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the absolute path to the CSV file
file_path = os.path.join(script_dir, "day4_ip.txt")

ip = open(file_path, "r").read()
lines = ip.splitlines()
rows = len(lines)
cols = len(lines[0])
directions = [
    (0, 1),  # Left to Right
    (0, -1),  # Right to Left
    (1, 0),  # Top to Bottom
    (-1, 0),  # Bottom to Top
    (1, 1),  # Diagonal (Top-left to Bottom-right)
    (-1, -1),  # Diagonal (Bottom-right to Top-left)
    (1, -1),  # Diagonal (Bottom-left to Top-right)
    (-1, 1),  # Diagonal (Top-right to Bottom-left)
]


def search_directions(row, col, searching_for, direction_tuple=(0, 0)):
    if searching_for == "M":
        for dir_row, dir_col in directions:
            search_row = row + dir_row
            search_col = col + dir_col

            if search_row < rows and search_col < cols:
                if lines[search_row][search_col] == searching_for:
                    return True, search_row, search_col, (dir_row, dir_col)
            else:
                pass
    else:
        search_row = row + direction_tuple[0]
        search_col = col + direction_tuple[1]
        if search_row < rows and search_col < cols:
            if lines[search_row][search_col] == searching_for:
                return (
                    True,
                    search_row,
                    search_col,
                    direction_tuple,
                )
            else:
                return (False, search_row, search_col, direction_tuple)
        else:
            pass


def search_directions(row, col, xmas_ct):
    for dir_row, dir_col in directions:
        search_row = row + dir_row
        search_col = col + dir_col
        ct = 0
        if (
            0 <= search_row < rows
            and 0 <= search_col < cols
            and lines[search_row][search_col] == "M"
        ):
            ct = ct + 1
            search_row = search_row + dir_row
            search_col = search_col + dir_col
            if (
                0 <= search_row < rows
                and 0 <= search_col < cols
                and lines[search_row][search_col] == "A"
            ):
                ct = ct + 1
                search_row = search_row + dir_row
                search_col = search_col + dir_col
                if (
                    0 <= search_row < rows
                    and 0 <= search_col < cols
                    and lines[search_row][search_col] == "S"
                ):
                    ct = ct + 1
                    search_row = search_row + dir_row
                    search_col = search_col + dir_col
                    if ct == 3:
                        xmas_ct += 1
    return xmas_ct


total_xmas_ct = 0
for row, lst in enumerate(lines):
    for col, element in enumerate(lst):
        if element == "X":
            xmas_ct = search_directions(row, col, xmas_ct=0)
            total_xmas_ct += xmas_ct
        else:
            pass

print(total_xmas_ct)


## Part 2
directions_p2 = [
    (1, 1),  # Diagonal (Top-left to Bottom-right)
    (-1, -1),  # Diagonal (Bottom-right to Top-left)
    (1, -1),  # Diagonal (Bottom-left to Top-right)
    (-1, 1),  # Diagonal (Top-right to Bottom-left)
]


def search_directions_p2(row, col):
    ct = 0
    if (
        (
            0 <= row + directions_p2[0][0] < rows
            and 0 <= col + directions_p2[0][1] < cols
            and 0 <= row + directions_p2[1][0] < rows
            and 0 <= col + directions_p2[1][1] < cols
            and lines[row + directions_p2[0][0]][col + directions_p2[0][1]] == "M"
            and lines[row + directions_p2[1][0]][col + directions_p2[1][1]] == "S"
        )
        or (
            0 <= row + directions_p2[1][0] < rows
            and 0 <= col + directions_p2[1][1] < cols
            and 0 <= row + directions_p2[0][0] < rows
            and 0 <= col + directions_p2[0][1] < cols
            and lines[row + directions_p2[0][0]][col + directions_p2[0][1]] == "S"
            and lines[row + directions_p2[1][0]][col + directions_p2[1][1]] == "M"
        )
    ) and (
        (
            0 <= row + directions_p2[2][0] < rows
            and 0 <= col + directions_p2[2][1] < cols
            and 0 <= row + directions_p2[3][0] < rows
            and 0 <= col + directions_p2[3][1] < cols
            and lines[row + directions_p2[2][0]][col + directions_p2[2][1]] == "M"
            and lines[row + directions_p2[3][0]][col + directions_p2[3][1]] == "S"
        )
        or (
            0 <= row + directions_p2[3][0] < rows
            and 0 <= col + directions_p2[3][1] < cols
            and 0 <= row + directions_p2[2][0] < rows
            and 0 <= col + directions_p2[2][1] < cols
            and lines[row + directions_p2[2][0]][col + directions_p2[2][1]] == "S"
            and lines[row + directions_p2[3][0]][col + directions_p2[3][1]] == "M"
        )
    ):
        # Your logic here
        ct = ct + 1

    return ct


mas_ct = 0
for row, lst in enumerate(lines):
    for col, element in enumerate(lst):
        if element == "A":
            xmas_ct = search_directions_p2(row, col)
            print(row, col, xmas_ct)

            mas_ct += xmas_ct
        else:
            pass
print(mas_ct)
