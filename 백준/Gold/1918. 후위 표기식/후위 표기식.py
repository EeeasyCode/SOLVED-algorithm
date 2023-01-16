words = input()
answer = ''
stack = []

for word in words:
  if word.isalpha():
    answer += word

  else:
    if word == '(':
      stack.append(word)
    
    elif word == '*' or word == '/':
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        answer += stack.pop()
      stack.append(word)
    
    elif word == '+' or word == '-':
      while stack and stack[-1] != '(':
        answer += stack.pop()
      stack.append(word)

    elif word == ')':
      while stack and stack[-1] != '(':
        answer += stack.pop()
      stack.pop()

while stack:
  answer += stack.pop()

print(answer)
        