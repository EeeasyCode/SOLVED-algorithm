# 사실 입력받으면서 할 수 있을 것 같기도? 굳이 이중배열?
# 첫째 줄 ~ 아홉번째 줄 -> 한 줄에 아홉 개 숫자
input_arr = [ list(map(int, input().split())) for _ in range(9)]

max_row, max_col = 0, 0

# 그냥 한 행 씩 받아서 max하고, 인덱스 검색해도 될듯?
max_num = float("-inf")

for row in range(9):
  for col in range(9):
    if max_num < max(max_num, input_arr[row][col]):
      max_row, max_col = row, col
      max_num = max(max_num, input_arr[row][col])

print(max_num)
print(f'{max_row+1} {max_col+1}')
# 해당 배열에서 가장 큰 최대 값
# 최대값이 위치한 행 번호와 열 번호 