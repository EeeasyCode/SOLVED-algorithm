N = int(input())
num_arr = list(map(int, input().split()))
arr = []
answer = 0

if N==1:
    num_arr.sort()
    answer = sum(num_arr[:5])

else:
    arr.append(min(num_arr[0], num_arr[5]))
    arr.append(min(num_arr[1], num_arr[4]))
    arr.append(min(num_arr[2], num_arr[3]))
    arr.sort()

    min_one = arr[0]
    min_two = arr[0] + arr[1]
    min_three = arr[0] + arr[1] + arr[2]

    one = (N-2)*(N-2) + 4*(N-1)*(N-2)
    two = 4*(N-2) + 4*(N-1)
    three = 4
    
    answer += min_one * one
    answer += min_two * two
    answer += min_three * three
print(answer)