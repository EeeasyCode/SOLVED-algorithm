def solution(phone_book):
    answer = True
    dict = {}
    
    for phone in phone_book:
        dict[phone] = 1
    
    for phone in phone_book:
        temp = ''
        for c in phone:
            temp += c
            if temp in dict and temp != phone:
                return False
    

    return True