total_count = 0
total = 0
while True:
  try :
    _, a, b = input().split()
    total_count += float(a)
    if b == 'A+':
      total += 4.5 * float(a)
    elif b == 'A0':
      total += 4.0 * float(a)
    elif b == 'B+':
      total += 3.5 * float(a)
    elif b == 'B0':
      total += 3.0 * float(a)
    elif b == 'C+':
      total += 2.5 * float(a)
    elif b == 'C0':
      total += 2.0 * float(a)
    elif b == 'D+':
      total += 1.5 * float(a)
    elif b == 'D0':
      total += 1.0 * float(a)
    elif b == 'P':
      total_count -= float(a)
    else:
      total += 0 * float(a)
    
  except EOFError:
    break

print(round(total/total_count, 6))