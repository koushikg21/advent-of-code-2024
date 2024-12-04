import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the absolute path to the CSV file
file_path = os.path.join(script_dir, "day2_ip.txt")

ip = open(file_path, "r").read()


## Part 1
ct = 0
flag = True
ind = 0
polarity_dict = {"+": 0, "-": 0}
for i in range(len(ip.split("\n"))):
    iList = ip.split("\n")[i].split(" ")
    while ind < len(iList) - 1:
        if abs(int(iList[ind + 1]) - int(iList[ind])) > 3:
            flag = False
            break
        if abs(int(iList[ind + 1]) - int(iList[ind])) == 0:
            flag = False
            break
        if int(iList[ind + 1]) - int(iList[ind]) > 0:
            polarity_dict["+"] = polarity_dict["+"] + 1
        if int(iList[ind + 1]) - int(iList[ind]) < 0:
            polarity_dict["-"] = polarity_dict["-"] + 1

        ind += 1

    if polarity_dict.get("+") > 0 and polarity_dict.get("-") > 0:
        flag = False

    if flag == False:
        flag = True
    else:
        ct = ct + 1
        print(iList)
    ind = 0
    polarity_dict = {"+": 0, "-": 0}

print("Part 1 " - ct)


## Part 2
def isSafe(iList):
    ct = 0
    flag = True
    ind = 0
    polarity_dict = {"+": 0, "-": 0}
    while ind < len(iList) - 1:
        if abs(int(iList[ind + 1]) - int(iList[ind])) > 3:
            flag = False
            break
        if abs(int(iList[ind + 1]) - int(iList[ind])) == 0:
            flag = False
            break
        if int(iList[ind + 1]) - int(iList[ind]) > 0:
            polarity_dict["+"] = polarity_dict["+"] + 1
        if int(iList[ind + 1]) - int(iList[ind]) < 0:
            polarity_dict["-"] = polarity_dict["-"] + 1

        ind += 1

    if polarity_dict.get("+") > 0 and polarity_dict.get("-") > 0:
        flag = False

    ind = 0
    polarity_dict = {"+": 0, "-": 0}

    return flag


final_ct = 0
for i in range(len(ip.split("\n"))):
    xx = ip.split("\n")[i].split(" ")
    flag = isSafe(xx)
    if flag == False:
        for ind, val in enumerate(xx):
            yy = xx.copy()
            yy.pop(ind)
            flag = isSafe(yy)
            if flag == True:
                final_ct += 1
                break
    else:
        final_ct += 1

print(f"Part 2 - {final_ct}")
