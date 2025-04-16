while True:
  vowel_count = 0
  input_str = input().lower()

  if input_str == '#': break
  
  # 입력 받은 문장의 모음 갯수 파악 (a, e, i, o, u) -> 대소문자 구분 X
  for vowel in ['a', 'e', 'i', 'o', 'u']:
    vowel_count += input_str.count(vowel)
  print(vowel_count)