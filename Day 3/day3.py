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

pattern = r"mul\(\s*\d+\s*,\s*\d+\s*\)"
matches = re.findall(pattern, ip)

print(matches)
