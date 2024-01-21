nums_arr=[]
for _ in range(9):
  n = int(input())
  nums_arr.append(n)

arr_sum = sum(nums_arr)
a, b = 0, 0

for i in range(8):
  for j in range(i+1, 9):
    if arr_sum - nums_arr[i] - nums_arr[j] == 100:
      a = nums_arr[i]
      b = nums_arr[j]
      
nums_arr.remove(a)
nums_arr.remove(b)
nums_arr.sort()

for num in nums_arr:
  print(num, end='\n')