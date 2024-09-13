import sys 
input = sys.stdin.readline

# N은 홀수
N = int(input())

num_arr = []

for _ in range(N):
    num_arr.append(int(input()))
num_arr.sort()

# 산술평균 출력
print(round(sum(num_arr) / N))

# 중앙값 출력
print(num_arr[(N-1)//2])

# 최빈값 출력
num_dict = {}
for num in num_arr:
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

max_count = max(num_dict.values())
max_count_num = []
for key, value in num_dict.items():
    if value == max_count:
        max_count_num.append(key)

if len(max_count_num) == 1:
    print(max_count_num[0])
else:
    print(max_count_num[1])

# 범위 출력
print(max(num_arr) - min(num_arr))
