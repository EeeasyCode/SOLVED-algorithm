N = int(input())
answer = 0

def check_group_word(str_arr):
  char_list = {}
  for idx, c in enumerate(str_arr):
    if c in char_list:
      if char_list[c] != idx - 1:
        return 0
    char_list[c] = idx
  return 1

for _ in range(N):
  str_arr = input()
  answer += check_group_word(str_arr)

print(answer)