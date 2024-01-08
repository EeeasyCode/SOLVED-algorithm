total_price = int(input())
total_cnt = int(input())
sum = 0
for _ in range(total_cnt):
  price, cnt = map(int, input().split())
  sum += price * cnt

if sum == total_price:
  print("Yes")
else:
  print("No")