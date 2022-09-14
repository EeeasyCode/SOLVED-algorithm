def solution(price, money, count):
    answer = 0
    result = 0
    for i in range(1, count+1):
        answer += price * i
    result = answer - money
    if (result <= 0):
        result = 0

    return result