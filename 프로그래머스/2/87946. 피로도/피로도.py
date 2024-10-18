answer = 0
def dfs(k, visit, count, dungeons):
    global answer
    
    if answer < count:
        answer = count
        
    for i, dungeon in enumerate(dungeons):
        if visit[i] != 1 and k >= dungeon[0]:
            visit[i] = 1
            dfs(k-dungeon[1], visit, count+1, dungeons)
            visit[i] = 0
    
    
def solution(k, dungeons):
    global answer
    visit = [0] * len(dungeons)
    count = 0
    
    dfs(k, visit, count, dungeons)
    
    return answer

# answer = 0

# def recur(k, dungeons, count, visit):
#     global answer
    
#     if answer < count:
#         answer = count
        
#     for i, dungeon in enumerate(dungeons):
#         if not visit[i] and k >= dungeon[0]:
#             visit[i] = True
#             recur(k-dungeon[1], dungeons, count+1, visit)
#             visit[i] = False

# def solution(k, dungeons):
#     global answer
#     count = 0
#     visit = [False] * len(dungeons)
#     recur(k, dungeons, count, visit)
    
#     return answer