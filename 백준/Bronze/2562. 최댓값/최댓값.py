num_arr = [int(input()) for _ in range(9)]

max_num = max(num_arr)
max_num_idx = num_arr.index(max_num) + 1

print(max_num)
print(max_num_idx)