def solution(babbling):
    answer = 0
    for bab in babbling:
        if not any(a in bab for a in ['ayaaya', 'yeye', 'woowoo', 'mama']):
            bab = bab.replace('aya', ' ')
            bab = bab.replace('ye', ' ')
            bab = bab.replace('woo', ' ')
            bab = bab.replace('ma', ' ')
            bab = bab.replace(' ', '')
            if bab == '':
                answer += 1
        
    return answer