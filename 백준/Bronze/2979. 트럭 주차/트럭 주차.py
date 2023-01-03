from collections import defaultdict

a, b, c = map(int, input().split())
answer = 0

time_dict = defaultdict(int)

for _ in range(3):
  t1, t2 = map(int, input().split())
  for i in range(t1, t2):
    time_dict[i] += 1

for t in time_dict.values():
  if t==1:
    answer += a
  elif t==2:
    answer += (b*2)
  else:
    answer += (c*3)
    
print(answer)
  

  