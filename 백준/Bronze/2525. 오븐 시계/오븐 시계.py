h, m = map(int, input().split())
add_time = int(input())

if add_time > 60:
    h += add_time // 60
    m += add_time % 60

else:
  m += add_time 
  
if m >= 60:
    h += 1
    m -= 60

print(h%24, m)