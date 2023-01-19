import sys

prime_num = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001):
    if check[i] == 0:
        prime_num.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = 1

T = int(sys.stdin.readline())

for _ in range(T):
    count = 0
    N = int(sys.stdin.readline())
    for i in prime_num:
        if i >= N:
            break
        if not check[N - i] and i <= N-i:  
            count += 1
    print(count)