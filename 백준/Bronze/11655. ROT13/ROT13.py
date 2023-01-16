S = input()
answer = ''
for s in S:
    if 65 <= ord(s) <= 90:
        key = ord(s) + 13
        if key > 90:
            key -= 26
        answer += chr(key)

    elif 97 <= ord(s) <= 122:
        key = ord(s) + 13
        if key > 122:
            key -= 26
        answer += chr(key)

    else:
        answer += s

print(answer)
