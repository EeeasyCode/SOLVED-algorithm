n= int(input())

memo_arr = []
memo_arr.append(0)
memo_arr.append(1)

for i in range(2, n+1):
    memo_arr.append(memo_arr[i-1] + memo_arr[i-2])

print(memo_arr[n])