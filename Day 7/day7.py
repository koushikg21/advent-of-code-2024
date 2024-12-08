import os
import operator
from itertools import product

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the absolute path to the CSV file
file_path = os.path.join(script_dir, "day7_ip.txt")

ip = open(file_path, "r").read()
ip = ip.splitlines()

arr = [operator.add, operator.mul]
# print(arr[0], "here-", arr[0](1, 2))
operator_combos = list(product(arr, repeat=2))

# Flatten the list of tuples into a single list
all_ops = [op for combo in operator_combos for op in combo]

# Print all values using map
# print(list(map(print, all_ops)))

final_ct = 0
pass_calc = 0
final_calc = 0
for line in ip:
    target = int(line.split(": ")[0])
    vals = [int(vals) for vals in line.split(": ")[1].split(" ")]
    operator_combos = list(product(arr, repeat=len(vals) - 1))

    for op in operator_combos:
        ind = 0
        while ind < len(vals) - 1:
            if ind == 0:
                calc = vals[ind]
            calc = op[ind](calc, vals[ind + 1])

            if target == calc and (ind == len(vals) - 2):
                pass_calc += 1
            ind += 1
    if pass_calc >= 1:
        final_calc += target
        pass_calc = 0


print(f"Part 1 - {final_calc}")


class custom_operator:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def concat(a, b) -> int:
        return int(str(a) + str(b))


arr = [operator.add, operator.mul, custom_operator.concat]
# print(arr[0], "here-", arr[0](1, 2))
operator_combos = list(product(arr, repeat=1))

arr[0]
final_ct = 0
pass_calc = 0
final_calc = 0
for line in ip:
    target = int(line.split(": ")[0])
    vals = [int(vals) for vals in line.split(": ")[1].split(" ")]
    operator_combos = list(product(arr, repeat=len(vals) - 1))

    for op in operator_combos:
        ind = 0
        while ind < len(vals) - 1:
            if ind == 0:
                calc = vals[ind]
            calc = op[ind](calc, vals[ind + 1])
            if target == calc and (ind == len(vals) - 2):
                pass_calc += 1
            ind += 1
    if pass_calc >= 1:
        final_calc += target
        pass_calc = 0
    print(final_calc)


print(f"Part 2 - {final_calc}")
