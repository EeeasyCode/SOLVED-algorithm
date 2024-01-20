def solution(sizes):
    answer = 0
    w_arr, h_arr = [], []
    for size in sizes:
        a, b = size
        if a < b:
            w_arr.append(a)
            h_arr.append(b)
        else:
            w_arr.append(b)
            h_arr.append(a)
        
    return max(w_arr) * max(h_arr)