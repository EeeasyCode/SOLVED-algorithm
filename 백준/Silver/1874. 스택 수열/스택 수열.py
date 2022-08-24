import sys
n = int(input())
stack = []
result = []
cnt = 0
X = True

for _ in range(n):
    num = int(sys.stdin.readline())
    
    while cnt < num :
        cnt += 1
        stack.append(cnt)
        result.append('+')
        
    if stack[-1] == num :
        stack.pop()
        result.append('-')
    else:
      X = False
      break
if X == False:
    print('NO')
else:
    for i in result:
        print(i)