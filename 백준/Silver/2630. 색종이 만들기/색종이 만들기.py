N = int(input())
answer = { 0: 0, 1: 0 }
whole_paper = [ list(map(int, input().split())) for _ in range(N) ]

def is_diff(x, y, size):
  for i in range(x, x + size):
    for j in range(y, y + size):
      if whole_paper[x][y] != whole_paper[i][j]:
        return True
  return False

def cut_recur(x, y, size):
  
  if size == 1:
    answer[whole_paper[x][y]] += 1
    return

  if not is_diff(x, y, size):
    answer[whole_paper[x][y]] += 1
    return
  
  mid = size // 2

  cut_recur(x, y, mid)
  cut_recur(x+mid, y, mid)
  cut_recur(x, y+mid, mid)
  cut_recur(x+mid, y+mid, mid)

cut_recur(0, 0, len(whole_paper))
for ans in answer.values():
  print(ans)