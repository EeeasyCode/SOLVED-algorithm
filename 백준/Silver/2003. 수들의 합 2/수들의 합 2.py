import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num_list = list(map(int, input().split()))

answer = 0
total_num = num_list[0]
start, end = 0, 1

while True:
    if total_num == m:
        total_num -= num_list[start]
        start += 1
        answer += 1
    elif total_num > m:
        total_num -= num_list[start]
        start += 1
    else:
        if end == n:
            break
        total_num += num_list[end]
        end += 1

print(answer)