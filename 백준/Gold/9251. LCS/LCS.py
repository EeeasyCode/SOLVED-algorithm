n = input()
m = input()

n_len = len(n) + 1
m_len = len(m) + 1
arr = [[0 for _ in range(n_len)] for _ in range(m_len)]

for i in range(1, m_len):
    for j in range(1, n_len):
        if n[j-1] == m[i-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i][j-1], arr[i-1][j])

print(arr[-1][-1])
