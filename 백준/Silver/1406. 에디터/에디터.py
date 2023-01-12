import sys

input = sys.stdin.readline

input_arr = list(input().strip())
n = int(input())
stack_arr = []

for _ in range(n):
    com_arr = input().strip()

    if com_arr[0] == 'P':
        input_arr.append(com_arr[2])
    elif com_arr[0] == 'L' and input_arr != []:
        stack_arr.append(input_arr.pop())
    elif com_arr[0] == 'D' and stack_arr != []:
        input_arr.append(stack_arr.pop())
    elif com_arr[0] == 'B' and input_arr != []:
        input_arr.pop()

print("".join(input_arr + list(reversed(stack_arr))))
