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


def calculate_sum(input_string):
    # Regex to extract valid instructions
    instruction_regex = r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))"

    # Extract all matches
    matches = re.findall(instruction_regex, input_string)

    # Initial state and sum
    enabled = True
    total_sum = 0

    # Process each instruction
    for match in matches:
        instruction = match[0]  # The full instruction

        if instruction.startswith("mul"):  # If it's a mul() operation
            a, b = int(match[1]), int(match[2])
            if enabled:  # Only process if enabled
                total_sum += a * b

        elif instruction == "do()":  # Re-enable
            enabled = True

        elif instruction == "don't()":  # Disable
            enabled = False

    return total_sum


# Example input
input_string = (
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
)

result = calculate_sum(ip)
print(f"Sum of enabled multiplications: {result}")
