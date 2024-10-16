def travel_mat(mat, park, start_row, start_col):
    for i in range(start_row, mat + start_row):
        for j in range(start_col, mat + start_col):
            if i < len(park) and j < len(park[0]):
                if park[i][j] != "-1":
                    return False
            else:
                return False    
    return True
	
def solution(mats, park):
    answer = 0
    R = len(park)
    C = len(park[0])
    mats.sort(reverse=True)
    
    for mat in mats:
        for r in range(R):
            for c in range(C):
                if travel_mat(mat, park, r, c):
                    return mat
                
    return -1