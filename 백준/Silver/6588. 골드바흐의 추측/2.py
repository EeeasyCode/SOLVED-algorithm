check_list = [True for i in range(1000001)]

for i in range(2, 1001):
    if check_list[i]:
        for j in range(i + i, 1000001, i):
            check_list[j] = False

while True:
    n = int(input())
    if n == 0:
        break

    for i in range(3, len(check_list)):
        if check_list[i] and check_list[n - i]:
            print(n, "=", i, "+", n - i)
            break
