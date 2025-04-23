import sys

input = sys.stdin.readline
N = int(input())
mem = [-1] * (N+1)

def fibo(n):
  if n == 0: return 0
  if n == 1: return 1
  if mem[n] != -1: return mem[n]
  
  mem[n] = fibo(n-1) + fibo(n-2)
  return mem[n]

print(fibo(N))