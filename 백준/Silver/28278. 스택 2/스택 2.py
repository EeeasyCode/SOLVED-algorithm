import sys
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
  oper = input().rstrip()

  if len(oper) != 1:
    _, x = oper.split(' ')
    x = int(x)
    stack.append(x)

  else:
    oper = int(oper)
    if oper == 2:
      if stack:
        print(stack.pop())
      else:
        print(-1)
    elif oper == 3:
      print(len(stack))
    elif oper == 4:
      if stack:
        print(0)
      else:
        print(1)
    elif oper == 5:
      if stack:
        print(stack[-1])
      else:
        print(-1)
  