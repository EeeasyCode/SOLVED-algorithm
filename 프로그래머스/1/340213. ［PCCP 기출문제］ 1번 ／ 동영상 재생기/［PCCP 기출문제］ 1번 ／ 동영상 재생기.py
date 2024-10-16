def str_to_time(str_time):
    mm, ss = map(int, str_time.split(':'))
    return mm*60 + ss

def solution(video_len, pos, op_start, op_end, commands):
    # 10초 전 이동 -> prev -> 10초 미만인 경우 처음 위치로 이동 (0분 0초)
    # 10초 후 이동 -> next -> 10초 미만인 경우 영상의 마지막 위치 (동영상 길이)
    # 오프닝 건너뛰기 -> 오프닝 구간인 경우 오프닝이 끝나는 위치로 이동
    
    answer = ''
    video_time = str_to_time(video_len)
    pos_time = str_to_time(pos)
    op_start_time = str_to_time(op_start)
    op_end_time = str_to_time(op_end)

    for command in commands:
        if command == 'next':
            if op_start_time <= pos_time <= op_end_time:
                pos_time = op_end_time
            pos_time = min(video_time, pos_time + 10)
        elif command == 'prev':
            pos_time = max(0, pos_time - 10)
        
        if op_start_time <= pos_time <= op_end_time:
            pos_time = op_end_time
            
    answer = f'{pos_time//60:02d}:{pos_time%60:02d}'
    return answer