nx, ny, w = input().split()
nx, ny, w = int(nx), int(ny), float(w)

while (nx, ny, w) != (0, 0, 0.0):
    x_arr = list(map(float, input().split()))
    x_arr = sorted(x_arr)
    dist_x = 0
    no_sign = True
    for x in x_arr:
        if x - (w/2) <= dist_x:
            dist_x = x + (w/2)
        else:
            no_sign = False
            break
    
    y_arr = list(map(float, input().split()))
    y_arr = sorted(y_arr)
    dist_y = 0
    for y in y_arr:
        if y - (w/2) <= dist_y:
            dist_y = y + (w/2)
        else:
            no_sign = False
            break
    
    if dist_x < 75 or dist_y < 100:
        print('NO')
    elif not no_sign:
        print('NO')
    
    if dist_x >= 75 and dist_y >= 100:
        print('YES')
    
    nx, ny, w = input().split()
    nx, ny, w = int(nx), int(ny), float(w)
