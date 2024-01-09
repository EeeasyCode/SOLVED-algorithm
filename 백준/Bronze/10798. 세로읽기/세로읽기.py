answer_arr = [[' ' for _ in range(15)] for _ in range(5)]

for i in range(5):
    str_arr = list(input())
    for j, str in enumerate(str_arr):
      answer_arr[i][j] = str

k =''

for i in range(15):
  for j in range(5):
    if answer_arr[j][i] != ' ':
      k += answer_arr[j][i]

print(k)