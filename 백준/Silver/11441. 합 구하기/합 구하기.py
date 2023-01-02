N = int(input())
arr1 = list(map(int, input().split()))


p_arr = [0]
for i in arr1:
  p_arr.append(p_arr[-1] + i)

answers = []
M = int(input())
for _ in range(M):
  a, b = map(int, input().split())
  answers.append(p_arr[b] - p_arr[a-1])

for answer in answers:
  print(answer)