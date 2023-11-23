import sys

n, m = map(int, sys.stdin.readline().split())

pocket_dict = dict()

for i in range(n):
	pocket_dict[i] = sys.stdin.readline().strip()
    
reverse_dict = {v:k for k,v in pocket_dict.items()}

for i in range(m):
	exam = sys.stdin.readline().strip()
	if exam.isdecimal():
		print(pocket_dict[int(exam)-1])
	else:
		print(reverse_dict[exam]+1)
