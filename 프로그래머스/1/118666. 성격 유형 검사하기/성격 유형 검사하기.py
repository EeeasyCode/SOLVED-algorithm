def solution(survey, choices):
    answer = ''
    choices_dict = {
        1: 3,
        2: 2,
        3: 1,
        4: 0,
        5: 1,
        6: 2,
        7: 3
    }
    survey_dict = {
        'R' : 0,
        'T' : 0,
        'C' : 0,
        'F' : 0,
        'J' : 0,
        'M' : 0,
        'A' : 0,
        'N' : 0
    }
    
    for i, s in enumerate(survey):
        s_1, s_2 = list(s)
        if 1 <= choices[i] <= 3:
            survey_dict[s_1] += choices_dict[choices[i]]
        if 5 <= choices[i] <= 7:
            survey_dict[s_2] += choices_dict[choices[i]]
            
    if survey_dict['R'] >= survey_dict['T']:
        answer += 'R'
    else:
        answer += 'T'
    
    if survey_dict['C'] >= survey_dict['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if survey_dict['J'] >= survey_dict['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    if survey_dict['A'] >= survey_dict['N']:
        answer += 'A'
    else:
        answer += 'N'
    
    return answer