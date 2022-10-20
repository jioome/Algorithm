import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# i번째 수 포함 
con = [[0]+[-1e9]*m for i in range(n+1)]
# i번째 수 미포함
notcon = [[0]+[-1e9]*m for i in range(n+1)]

for i in range(1, n+1):
    num = int(input())
    for j in range(1, min(m, (i+1)//2)+1):
        # i번째 수 미포함 하는 j개 구간합 
        notcon[i][j]=max(con[i-1][j], notcon[i-1][j])
        # 구간끼리 겹쳐있을 수 없으니까 notcon[i-1][j-1]
        con[i][j]=max(con[i-1][j], notcon[i-1][j-1])+num

# 마지막 원소 포함한 구간 최대값, 마지막 거 뺀 구간합
print(max(con[n][m], notcon[n][m]))
