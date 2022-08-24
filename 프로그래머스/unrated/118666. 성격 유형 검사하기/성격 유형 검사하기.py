def solution(survey, choices):
    answer = ''
    data = {'R': 0, 'T': 0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i in range(len(survey)):
        a,b = survey[i][0], survey[i][1]
        
        if (choices[i] < 4):
            data[a] += 4 - choices[i]
        elif (choices[i] > 4):
            data[b] += choices[i] - 4
        
    if (data['R'] >= data['T']):
        answer += 'R'
    else:
        answer += 'T'
    if (data['C'] >= data['F']):
        answer += 'C'
    else:
        answer += 'F'
    if (data['J'] >= data['M']):
        answer += 'J'
    else:
        answer += 'M'
    if (data['A'] >= data['N']):
        answer += 'A'
    else:
        answer += 'N'
    
    return answer