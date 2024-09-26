S, K = map(int, input().split())
answer_arr = []

while K > 0:
    average = S // K
    answer_arr.append(average)
    S -= average
    K -= 1

answer = answer_arr[0]
for i in range(1, len(answer_arr)):
    answer *= answer_arr[i]

print(answer)