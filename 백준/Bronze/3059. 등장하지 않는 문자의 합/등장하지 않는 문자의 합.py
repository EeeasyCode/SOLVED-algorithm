N = int(input())

for _ in range(N):
    S = set(input())
    ALPHABET_SET = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    NON_INPUT_ALPHABET_SET = ALPHABET_SET - S
    answer = 0
    
    for i in NON_INPUT_ALPHABET_SET:
        answer += ord(i)
    print(answer)
