import sys
input = sys.stdin.readline 

n,k = map(int,input().split())
bag = [[0,0]]
for i in range(n):
    bag.append(list(map(int,input().split())))
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1,n+1): # 버틸 수 있는 물품 수 
    for j in range(1,k+1): # 버틸 수 있는 무게
        w = bag[i][0] # 물건 무게 
        v = bag[i][1] # 가치
        if w > j:
            dp[i][j] = dp[i-1][j]
        else : 
            dp[i][j] = max(dp[i-1][j-w]+v,dp[i-1][j])

print(dp[n][k])

