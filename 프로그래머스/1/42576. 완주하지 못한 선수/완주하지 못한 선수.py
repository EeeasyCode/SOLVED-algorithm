def solution(participant, completion):
    answer = ''
    part_dict = dict()
    for part in participant:
        if part in part_dict.keys():
            part_dict[part] += 1
        else:
            part_dict[part] = 1
    
    for com in completion:
        if part_dict[com]:
            part_dict[com] -= 1
            
    for k, v in part_dict.items():
        if v != 0:
            answer = k
    
    return answer