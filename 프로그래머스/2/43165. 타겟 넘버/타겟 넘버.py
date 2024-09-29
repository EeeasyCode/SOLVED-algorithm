def solution(numbers, target):
    # BFS
    # 이진 트리로 생각 후 너비 우선 탐색
    leaves = [0]
    answer = 0
    
    for num in numbers:
        temp = []
        
        for leave in leaves:
            temp.append(leave + num)
            temp.append(leave - num)
        leaves = temp
    
    for leave in leaves:
        if leave == target:
            answer += 1
    
    return answer