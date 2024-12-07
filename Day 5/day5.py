import os
import pandas as pd

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the absolute path to the CSV file
file_path = os.path.join(script_dir, "day5ip_1.txt")

file_path2 = os.path.join(script_dir, "day5ip_2.txt")

ip = open(file_path, "r").read()
ip_2 = open(file_path2, "r").read()
ip_2 = ip_2.splitlines()
good_list = []
xx = [line.split("|") for line in ip.split("\n")]
final_ct = 0
yy = pd.DataFrame(xx, columns=["key", "value"])
for i in range(len(ip_2)):
    row_val = ip_2[i].split(",")
    ct = 0
    for j in range(len(row_val) - 1):
        try:
            lkup_list = list(yy[yy["key"] == row_val[j]]["value"])
            if row_val[j + 1] in lkup_list:
                ct = ct + 1
        except:
            pass
    if ct == len(row_val) - 1:
        good_list.append(i)
        a = int(ct / 2)
        final_ct = final_ct + int(row_val[a])
print(f"Part 1 - {final_ct}")


## Part 2

bad_list: list[str] = [
    "".join(ip_2[ind]) for ind in range(len(ip_2)) if ind not in good_list
]
ip_dict = yy.groupby("key")["value"].apply(list).to_dict()
# print(ip_dict)


part2_ct = 0
for ind in range(len(bad_list)):
    row_val = bad_list[ind].split(",")
    updated_rowval = row_val.copy()
    j = 0
    while j <= len(row_val) - 1:
        #    print(row_val)
        if j + 1 >= len(updated_rowval):
            break
        try:
            if updated_rowval[j + 1] in ip_dict.get(updated_rowval[j]):
                # print(row_val[j + 1], "Present")
                j += 1
                pass
            else:
                # print(row_val[j + 1], "Not Present")]
                temp = updated_rowval[j]
                updated_rowval[j] = updated_rowval[j + 1]
                updated_rowval[j + 1] = temp
                j = 0

        except:
            temp = updated_rowval[j]
            updated_rowval[j] = updated_rowval[j + 1]
            updated_rowval[j + 1] = updated_rowval[len(updated_rowval) - 1]
            updated_rowval[len(updated_rowval) - 1] = temp
            j = 0

    midpt = int((len(updated_rowval) - 1) / 2)
    part2_ct = part2_ct + int(updated_rowval[midpt])

print(part2_ct)
