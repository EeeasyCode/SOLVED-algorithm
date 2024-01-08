a_str = input()

count = 0

for i in range(len(a_str)//2):
  if a_str[i] == a_str[-(i+1)]:
    count += 1

if count == len(a_str)//2:
  print("1")
else:
  print("0")