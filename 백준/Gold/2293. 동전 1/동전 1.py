import sys 
input =sys.stdin.readline
n,k = map(int,input().split())
coin= []
for _ in range(n):
    coin.append(int(input()))
dp = [0]*(k+1)
# 동전 하나 사용하는 경우 
# coin 3 일 때 dp[3-3] = 1 로 맞춤
dp[0] = 1 
for c in coin:
    for i in range(c, k+1):
        dp[i] += dp[i-c]
print(dp[-1])



