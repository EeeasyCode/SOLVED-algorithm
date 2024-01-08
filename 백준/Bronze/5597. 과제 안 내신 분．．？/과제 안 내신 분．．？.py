arr = [0] * 30
for i in range(30):
  arr[i] = i+1
  
for _ in range(28):
  a_arr = []
  a = int(input())
  a_arr.append(a)
  arr = list(set(arr) - set(a_arr))

arr.sort()
print(arr[0])
print(arr[1])
