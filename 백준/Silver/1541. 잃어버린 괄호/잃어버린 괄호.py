In = input().split('-')
sum = 0

for i in In[0].split('+'):
  sum += int(i)
#- 기준으로 나눠진 배열 첫번째를
#더해준다

for i in In[1:]:
  for j in i.split('+'):
    sum -= int(j)
#나머지 수는 전부 빼준다

print(sum)


