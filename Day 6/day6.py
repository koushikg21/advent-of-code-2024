import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the absolute path to the CSV file
file_path = os.path.join(script_dir, "day6ip.txt")


ip = open(file_path, "r").read()
ip = ip.split("\n")

rows = len(ip[0])
cols = len(ip)

for i in range(cols):
    for j in range(rows):
        if ip[i][j] == "^":
            loc_i = i
            loc_j = j


directions = [
    (-1, 0),  # Bottom to Top
    (0, 1),  # Left to Right
    (1, 0),  # Top to Bottom
    (0, -1),  # Right to Left
]

found = 1
directions_i = 0
loc_store = []
while found == 1 and 0 <= loc_i < rows and 0 <= loc_j < cols:
    row_dir = directions[directions_i][0]
    col_dir = directions[directions_i][1]

    if ip[loc_i][loc_j] == "#":
        loc_i = loc_i - row_dir
        loc_j = loc_j - col_dir
        if directions_i == 3:
            directions_i = 0
        else:
            directions_i += 1
    else:
        loc_i = loc_i + row_dir
        loc_j = loc_j + col_dir
        try:
            if ip[loc_i][loc_j] != "#":
                loc_store.append([loc_i, loc_j])
        except:
            pass

    if loc_i == rows or loc_j == cols:
        found = 0
distint_locs = set(tuple(loc) for loc in loc_store)

print(len(distint_locs))
# and 0 <= loc_i < rows and 0 <= loc_j <= cols
## Find marker
