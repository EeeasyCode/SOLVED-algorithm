def solution(dirs):
    answer = set()
    x, y = 0, 0
    for dir in dirs:
        nx, ny = update_dot(x, y, dir)
        if not validate_dot(nx, ny):
            continue
        answer.add((x, y, nx, ny))
        answer.add((nx, ny, x, y))
        x, y = nx, ny
    print(answer)
    return len(answer)//2

def validate_dot(x, y):
    return -5 <= x <= 5 and -5 <= y <= 5
    
def update_dot(x, y, dir):
    if dir == 'U':
        nx, ny = x, y+1
    
    if dir == 'D':
        nx, ny = x, y-1
    
    if dir == 'R':
        nx, ny = x+1, y
        
    if dir == 'L':
        nx, ny = x-1, y
    
    return nx, ny