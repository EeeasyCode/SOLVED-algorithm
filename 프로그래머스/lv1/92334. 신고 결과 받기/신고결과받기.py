from collections import defaultdict

def solution(id_list, report,k):
    answer = []
    setReport = list(set(report))
    singo = defaultdict(set)
    card = defaultdict(int)
	
    for i in setReport:
        a,b = i.split()
        singo[a].add(b)
        card[b] += 1
    
    for i in id_list:
        cnt = 0
        
        for u in singo[i]:
            if card[u]>=k:
                cnt +=1
        answer.append(cnt)
    return answer
