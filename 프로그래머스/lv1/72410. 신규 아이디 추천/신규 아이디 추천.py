import re

def solution(new_id):
    answer = ''
    step1 = new_id.lower()
    step2 = re.sub('[^a-z-_\.0-9]', '', step1)
    step3 = re.sub('(([.])\\2{1,})', '.', step2)
    step4 = step3.strip('.')
    step5 = ''
    if step4 == '':
        step5 = 'a'
    else:
        step5 = step4
    step6 = ''
    if (len(step5) > 15):
        step6 = step5[0:15].strip('.')
        
    else:
        step6 = step5
    
    if(len(step6) < 3):
        answer = step6
        while(len(answer) < 3):
            answer += step6[-1]
    else:
        answer = step6
    
    return answer