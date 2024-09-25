import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
num_arr = list(map(int, input().rstrip().split()))

def bubble_sort(N, K, num_arr):
    count = 0
    for i in range(N, 1, -1):
        for j in range(i-1):
            if num_arr[j] > num_arr[j+1]:
                num_arr[j], num_arr[j+1] = num_arr[j+1], num_arr[j]
                count += 1
                if count == K:
                    return(print(num_arr[j], num_arr[j+1]))
    return(print(-1))

bubble_sort(N, K, num_arr)
