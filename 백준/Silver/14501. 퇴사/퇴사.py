import sys

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(20)
dp[time[0][0]-1] = time[0][1]

for i in range(1, n):
    t = time[i][0]
    p = time[i][1]
    if (i+t-1) > n:
        continue
    # 더해서 그 시간으로 간 거 ,그 전 반복에서 더해져서 dp[i+t-1] 자리에 들어있는 거
    dp[i+t-1] = max(max(dp[:i]) + p, dp[i+t-1])


print(max(dp[:n]))
