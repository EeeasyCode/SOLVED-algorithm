def solution(phone_number):
    answer = ''
    phone_number = list(phone_number)
    for i in range(len(phone_number)-4):
        phone_number[i] = '*'
    return ''.join(phone_number)