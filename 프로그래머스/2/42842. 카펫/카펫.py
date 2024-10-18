def solution(brown, yellow):
    answer = []
    w = brown // 2 - 1
    h = 3
    
    while (w * h) - brown != yellow:
        w -= 1
        h += 1
    
    return [w, h]