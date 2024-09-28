N = int(input())

hotKey_dict = {}

for _ in range(N):
    S = input()
    S_list = list(S)
    S_arr = list(S.split(' '))
    
    key_status = False
    idx = 0
    
    for s in S_arr:
        s_first = s[0].lower()
        if not hotKey_dict.get(s_first):
            hotKey_dict[s_first] = 1
            idx = S.index(s, idx)
            key_status = True
            break
        else:
            idx += len(s)

    if key_status == False:
        for s in S:
            s_first = s[0].lower()
            if not hotKey_dict.get(s_first) and s_first.isalpha():
                hotKey_dict[s_first] = 1
                idx = S.index(s)
                key_status = True
                break
    
    if key_status == False:
        print(S)
    else:
        print(''.join(S[:idx]) + '[' + str(S[idx]) + ']' + ''.join(S[idx+1:]))
    
