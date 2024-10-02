def solution(tickets):
    answer = []
    visit = [False] * len(tickets)
    
    def dfs(start, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return
        
        for index, ticket in enumerate(tickets):
            if ticket[0] == start and not visit[index]:
                visit[index] = True
                dfs(ticket[1], path + [ticket[1]])
                visit[index] = False
    
    dfs("ICN", ["ICN"])
    
    answer.sort()
    
    return answer[0]