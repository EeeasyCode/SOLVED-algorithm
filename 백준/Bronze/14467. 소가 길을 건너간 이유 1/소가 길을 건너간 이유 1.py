N = int(input())

cow_list = [0] * 11
now_list = [-1] * 11

for _ in range(N):
    a, b = map(int, input().split())
    if now_list[a] == -1:
        now_list[a] = b
    elif now_list[a] != b:
        cow_list[a] += 1
        now_list[a] = b 

print(sum(cow_list))