from collections import defaultdict

alpha_dict = defaultdict(int)

for i in range(26):
  alpha_dict[i] = 0

S = input()
S = S.upper()

for s in S:
  
  alpha_dict[ord(s) - ord('A')] += 1


for i in alpha_dict.values():
  print(i, end=' ')
