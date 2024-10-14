from functools import reduce
import operator

def solution(clothes):
    answer = 1
    clothe_dict = {}
    
    for clothe in clothes:
        if clothe[1] in clothe_dict.keys():
            clothe_dict[clothe[1]] += 1
        else:
            clothe_dict[clothe[1]] = 1

    
    for _, v in clothe_dict.items():
        answer *= (v+1)
        
    return answer - 1