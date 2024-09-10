N, M = map(int, input().split())

answer_arr = [0] * N

for i in range(1, N+1):
    answer_arr[i-1] = i

for _ in range(M):
    i, j = map(int, input().split())
    answer_arr[i-1], answer_arr[j-1] = answer_arr[j-1], answer_arr[i-1]

for answer in answer_arr:
    print(answer, end=' ')