t = int(input())

def gcd_func(a:int, b:int) -> int:
  if b == 0:
    return a
  else:
    return gcd_func(b, a%b)
    
for _ in range(t):
  total = 0
  nums = list(map(int, input().split()))
  n = nums.pop(0)

  for i in range(n-1):
    for j in range(i+1, n):
      a, b = nums[i], nums[j]
      total += gcd_func(a, b)
    
  print(total)  


  
  