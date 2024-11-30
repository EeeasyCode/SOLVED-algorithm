import sys
input = sys.stdin.readline

n = int(input())

# 이름 국어 영어 수학
score_dict = {}

for _ in range(n):
    name, korean, english, math = input().split()
    score_dict[name] = (int(korean), int(english), int(math))

# 딕셔너리의 items를 정렬
sorted_scores = sorted(score_dict.items(), key=lambda x: (-x[1][0], x[1][1], -x[1][2], x[0]))

# 결과 출력
for name, _ in sorted_scores:
    print(name)