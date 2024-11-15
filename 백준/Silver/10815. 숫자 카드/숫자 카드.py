import sys
input = sys.stdin.readline

N = int(input())

sang_have_list = list(map(int, input().split()))
sang_have_dict = {}

for sang_have in sang_have_list:
    sang_have_dict[sang_have] = 1

M = int(input())
do_have_list = list(map(int, input().split()))

for i, val in enumerate(do_have_list):
    if val in sang_have_dict:
        do_have_list[i] = 1
    else:
        do_have_list[i] = 0

for answer in do_have_list:
    print(answer, end=' ')

