def solution(today, terms, privacies):
    answer = []
    term_dict={}
    year, month, day=map(int, today.split('.'))
    
    for term in terms:
        alphabet, number=term.split()
        term_dict[alphabet]=int(number)
    
    for i in range(len(privacies)):
        date, alphabet=privacies[i].split()
        d_year, d_month, d_day=map(int, date.split('.'))
        d_month+=term_dict[alphabet]
        while d_month>12:
            d_month-=12
            d_year+=1
        
        if d_year>year:
            continue
            
        elif d_year==year:
            if d_month>month:
                continue
                
            elif d_month==month:
                if d_day>day:
                    continue
                    
        answer.append(i+1)
        
    return answer