N = int(input())
words = input()
int_arr = [0] * N

for i in range(N):
  int_arr[i] = int(input())
  
stack = []
for word in words:
  if word.isalpha():
    stack.append(int_arr[ord(word) - ord('A')])

  else:
    str_2 = stack.pop()
    str_1 = stack.pop()

    if word == '+':
      stack.append(str_1 + str_2)
    elif word == '-':
      stack.append(str_1 - str_2)
    elif word == '*':
      stack.append(str_1 * str_2)
    else:
      stack.append(str_1 / str_2)

print('%.2f' %stack[0])