import sys
input = sys.stdin.readline

n = input().strip()
digits = list(n)

if '0' not in digits:
    print(-1)
else:
    total = sum(map(int, digits))
    if total % 3 != 0:
        print(-1)
    else:
        digits.sort(reverse=True)
        print(''.join(digits))