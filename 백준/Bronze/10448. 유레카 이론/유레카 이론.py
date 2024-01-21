tri_dict = [0 for _ in range(45)]
tri_dict[0]=0

for n in range(1, 45):
  tri_dict[n] = tri_dict[n-1] + n

answer = [0 for _ in range(1001)]
for i in tri_dict[1:]:
  for j in tri_dict[1:]:
    for k in tri_dict[1:]:
      if i+j+k<=1000:
        answer[i+j+k] = 1

k = int(input())
for _ in range(k):
  n = int(input())
  if answer[n] == 1:
    print(1)
  else:
    print(0)
          
          
  