import sys
input = sys.stdin.readline

N, M = map(int, input().split())

no_hear_people = []
no_see_people = []

for _ in range(N):
    no_hear_people.append(input().rstrip())

for _ in range(M):
    no_see_people.append(input().rstrip())

no_hear_people = set(no_hear_people)
no_see_people = set(no_see_people)

answer_list = list(no_hear_people & no_see_people)
answer_list.sort()

print(len(answer_list))
for i in answer_list:
    print(i)
