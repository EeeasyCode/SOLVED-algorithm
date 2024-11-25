import sys
input = sys.stdin.readline

n, m = map(int, input().split())

password_dict = {}

for _ in range(n):
    id_str, password = input().split()
    password_dict[id_str] = password

for _ in range(m):
    find_password = input().rstrip()
    print(password_dict[find_password])