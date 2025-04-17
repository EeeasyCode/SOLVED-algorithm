N = int(input())
answer = 0
for _ in range(N):
  word = input()
  prev = word[0]
  isNotGroupWord = False

  for i in range(1, len(word)):
    if word[i] == prev:
      continue
    
    if prev in word[i:]:
      isNotGroupWord = True
      break

    else:
      prev = word[i]
  
  if not isNotGroupWord:
    answer += 1

print(answer)
 