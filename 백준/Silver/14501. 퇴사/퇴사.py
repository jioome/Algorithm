import sys

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(21)
dp[time[0][0]-1] = time[0][1]

for i in range(1, n):
    t = time[i][0]
    p = time[i][1]

    dp[i+t-1] = max(max(dp[:i]) + p, dp[i+t-1])


print(max(dp[:n]))
