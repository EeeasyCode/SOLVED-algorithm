import re

def solution(s):
    answer = 0
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        s = re.sub(num[i], str(i), s)
    answer = int(s)
