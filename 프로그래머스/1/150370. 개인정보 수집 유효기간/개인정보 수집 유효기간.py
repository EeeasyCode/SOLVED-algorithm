def solution(today, terms, privacies):
    answer = []
    term_hash = {}
    
    for term in terms:
        term_type, date = term.split()
        term_hash[term_type] = int(date)
    
        
    for idx, privacy in enumerate(privacies):
        p_date, p_type = privacy.split()
        
        t_date = term_hash[p_type]
        
        p_year, p_month, p_day = map(int, p_date.split('.'))
        
        p_day -= 1
        
        if p_day == 0:
            p_day = 28
            p_month -= 1
            
            if p_month == 0:
                p_year -= 1
                p_month = 12
                
        p_month += t_date
        
        if p_month > 12:
            p_year += p_month // 12
            if p_month % 12 == 0:
                p_year -= 1
                p_month = 12;
            else:
                p_month %= 12
        
        now_year, now_month, now_day = map(int, today.split('.'))
        
        if now_year > p_year:
            answer.append(idx+1)
            continue
            
        if now_year == p_year and now_month > p_month:
            answer.append(idx+1)
            continue
            
        if now_year == p_year and now_month == p_month and now_day > p_day:
            answer.append(idx+1)
            continue
            
    return answer