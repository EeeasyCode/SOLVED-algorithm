dist = int(input())

dist = dist % 100
answer = -1

if dist==0 or dist==10 or dist==30 or dist==60:
    answer = 0
elif 75 < dist < 85:
    answer = 4
elif 40 < dist < 50 or 70 < dist <= 75 or 85 <= dist < 90:
    answer = 3
elif 15 < dist < 25 or 35 < dist <= 40 or 50 <= dist < 55 or 65 < dist <= 70 or 90 <= dist < 95:
    answer = 2
else:
    answer = 1

print(answer)