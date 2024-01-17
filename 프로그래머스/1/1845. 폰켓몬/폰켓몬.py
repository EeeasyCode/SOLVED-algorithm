def solution(nums):
    answer = {}
    for num in nums:
        if num in answer:
            answer[num] += 1
        else:
            answer[num] = 1
    cnt = 0
    a = []
    for k, v in answer.items():
        if cnt == len(nums)//2:
            break
        if v != 0:
            a.append(k)
            answer[k] -= 1
            cnt += 1
    print(a)
    return len(list(set(a)))