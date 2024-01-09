find_data = list(map(int, input().split()))
origin_data = [1, 1, 2, 2, 2, 8]
answer_data = [0] * 6
for i, data in enumerate(origin_data):
  answer_data[i] = data - find_data[i]

for answer in answer_data:
  print(answer, end=' ')
    