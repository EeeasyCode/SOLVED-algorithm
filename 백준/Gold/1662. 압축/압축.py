def decode(start, end):
  total_len = 0
  while(start<=end):
    total_len += 1
    if S[start] == '(':
      total_len -= 2
      repeat = int(S[start-1])
      depth = 1
      closing_idx = start + 1
      while depth:
        if S[closing_idx] == '(': depth += 1
        elif S[closing_idx] == ')': depth -= 1
        closing_idx += 1      
      total_len += decode(start+1, closing_idx-2) * repeat
      start = closing_idx
    else:
      start += 1
  return total_len

S = input()
print(decode(0, len(S)-1))