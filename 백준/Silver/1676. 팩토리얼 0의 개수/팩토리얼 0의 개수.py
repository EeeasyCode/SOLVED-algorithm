import sys
input = sys.stdin.readline

N = int(input())

# 팩토리얼 계산
def fact(n):
    if n<=1:
        return 1
    
    return n * fact(n-1)

fact_output = fact(N)
output_list = list(str(fact_output))

output_list.reverse()
count = 0

for num in output_list:
    if int(num) == 0:
        count += 1
    else:
        break

print(count)

    

