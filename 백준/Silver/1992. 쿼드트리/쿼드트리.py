N = int(input())
whole_data = [ list(map(int, list(input().rstrip()))) for _ in range(N) ]

def is_diff(x, y, size):
  for i in range(x, x + size):
    for j in range(y, y + size):
      if whole_data[x][y] != whole_data[i][j]:
        return True
  return False

def cut_recur(x, y, size):    
  if not is_diff(x, y, size):
    return str(whole_data[x][y])
  
  mid = size // 2
  
  return "(" + \
          cut_recur(x, y, mid) + \
          cut_recur(x, y+mid, mid) + \
          cut_recur(x+mid, y, mid) + \
          cut_recur(x+mid, y+mid, mid) + \
          ")"

print(cut_recur(0, 0, N))
