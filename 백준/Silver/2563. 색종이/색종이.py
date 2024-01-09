answer = [[0 for _ in range(101)] for _ in range(101)]

N = int(input())
for _ in range(N):
  x, y = map(int, input().split())
  for i in range(x, x+10):
    for j in range(y, y+10):
      answer[i][j] = 1

answer_cnt = 0
for i in answer:
  answer_cnt += i.count(1)
print(answer_cnt)
