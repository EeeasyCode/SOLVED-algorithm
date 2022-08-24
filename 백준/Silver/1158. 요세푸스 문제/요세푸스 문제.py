n, k = map(int, input().split())
que = [i for i in range(1, n+1)]

result = []
num = 0

for _ in range(n):
    num += k-1
    if num >= len(que):
      num = num%len(que)
  
    result.append(str(que.pop(num)))

print('<',', '.join(result),'>',sep='')

