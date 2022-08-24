n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]

#같은 색을 연달아 칠할 수 없으므로 만약에 현재 빨간색이면, 이전 초록, 파란색 비용 중 작은 비용으로 선택
for i in range(1,n):
    a[i][0]=a[i][0]+min(a[i-1][1],a[i-1][2])
    a[i][1]=a[i][1]+min(a[i-1][0],a[i-1][2])
    a[i][2]=a[i][2]+min(a[i-1][0],a[i-1][1])

print(min(a[n-1]))