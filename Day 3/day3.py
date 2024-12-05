import os
import re

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the absolute path to the CSV file
file_path = os.path.join(script_dir, "day3_ip.txt")

ip = open(file_path, "r").read()

pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"

# Find all matches
matches = re.findall(pattern, ip)
cal = 0
for tp in matches:
    cal = cal + int(tp[0]) * int(tp[1])

print(cal)


## Part 2

import re


text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
# Regex to match all `mul(a,b)` with or without valid parentheses

# Regex to match all potential mul(a,b) patterns
pattern = r"(\w*mul)\((\d+),(\d+)\)"

# Find all matches
all_matches = re.findall(pattern, text)
print(all_matches)
