N = int(input())
    
participant_arr = ["SK", "CY"]
dp_arr = [-1] * 1001

dp_arr[1], dp_arr[2], dp_arr[3], dp_arr[4] = 0, 1, 0, 0

for i in range(5, N+1):
    if dp_arr[i-1] == 1 or dp_arr[i-3] == 1 or dp_arr[i-4] == 1:
        dp_arr[i] = 0
    else:
        dp_arr[i] = 1

print(participant_arr[dp_arr[N]])