str = input()
test = ''
for s in str:
    if s.isupper():
        test += s.lower()
    else:
        test += s.upper()
print(test)