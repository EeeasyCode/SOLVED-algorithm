N = int(input())
slime_arr = list(map(int, input().split()))
slime_arr.sort(reverse=True)
answer = 0
while len(slime_arr) > 1:
    slime_x, slime_y = slime_arr.pop(), slime_arr.pop()
    answer += slime_x * slime_y
    slime_arr.append(slime_x + slime_y)
    slime_arr.sort(reverse=True)

print(answer)