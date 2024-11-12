N = int(input())
str_list = []

for _ in range(N):
    str_list.append(input())

str_list = list(set(str_list))
answer = sorted(str_list, key = lambda x : (len(x), x))


for s in answer:
    print(s)
