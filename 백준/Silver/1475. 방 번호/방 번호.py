import sys
input = sys.stdin.readline

num = input().rstrip()

set_dict = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0 }

for i in num:
    if i == '6' or i == '9':
        if set_dict[6] >= set_dict[9]:
            set_dict[9] += 1
        else:
            set_dict[6] += 1
    else:
        set_dict[int(i)] += 1

print(max(set_dict.values()))