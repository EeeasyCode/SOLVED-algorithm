# N*M 크기의 행렬 A, B -> 더한 행렬
# 입력 -> N, M (행렬의 크기)
# 입력 -> 행렬 A -> 행렬 B
N, M = map(int, input().split())
answer_arr = [[0 for _ in range(M)] for _ in range(N)]

a_arr = [ list(map(int, input().split())) for _ in range(N) ]
b_arr = [ list(map(int, input().split())) for _ in range(N) ]

for row in range(N):
  for col in range(M):
    answer_arr[row][col] = a_arr[row][col] + b_arr[row][col]

for data in answer_arr:
  print(*data)