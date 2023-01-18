def eratos(n: int, k: int) -> int:
    check_list = [True] * (n + 1)
    cnt = 0

    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            if check_list[j] == True:
                check_list[j] = False
                cnt += 1
                if cnt == k:
                    return j


n, k = map(int, input().split())
print(eratos(n, k))
