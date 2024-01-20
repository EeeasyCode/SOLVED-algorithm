def solution(citations):
    answer = [0]
    
    for h in range(len(citations)+1):
        count = 0
        for citation in citations:
            if citation >= h:
                count += 1
                
            if h == count:
                answer.append(count)
                
    return max(answer)