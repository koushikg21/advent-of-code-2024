import os
import pandas as pd

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the absolute path to the CSV file
file_path = os.path.join(script_dir, "day1_ip.csv")

ip = pd.read_csv(file_path)

sorted_l = sorted(ip["l"])
sorted_r = sorted(ip["r"])

sum_diff = 0
count_repeat = 0
for i in range(len(sorted_l)):
    diff = abs(sorted_l[i] - sorted_r[i])
    sum_diff = sum_diff + diff

print(f"Part 1 - {sum_diff}")

sum_diff = 0
count_repeat = 0
for i in range(len(sorted_l)):
    for j in range(len(sorted_r)):
        if sorted_l[i] == sorted_r[j]:
            count_repeat = count_repeat + 1
    sum_diff = sum_diff + sorted_l[i] * count_repeat
    count_repeat = 0

print(f"Part 2 - {sum_diff}")
