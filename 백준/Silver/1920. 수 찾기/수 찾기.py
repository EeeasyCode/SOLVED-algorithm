from bisect import *

def bs(A, find_num):
  existIdx = bisect_left(A, find_num)

  if (existIdx < len(A) and A[existIdx] == find_num): return 1
  else: return 0
  

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
findNumArr = list(map(int, input().split()))

for find_num in findNumArr:
  print(bs(A, find_num))