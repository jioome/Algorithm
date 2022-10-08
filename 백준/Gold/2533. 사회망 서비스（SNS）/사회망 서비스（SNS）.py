import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
graph = [[]for _ in range(n+1)]
# n+1 하는 이유
visited = [0]*(n+1)

for i in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

# 정점번호, 얼리어답터 체크
dp = [[0,0] for _ in range(n+1)]

def solve_dp(num):
    visited[num]=1
    dp[num][0] = 0 # 얼리어답터가 아닌 경우 
    dp[num][1] = 1 # (자기 포함)정점 번호가 num이고 자신이 얼리어답터인 경우
    for i in graph[num]:
        if not visited[i] :
            
            solve_dp(i)
            # 얼리어답터 아닐 때 
            dp[num][0] += dp[i][1]
        
            # 얼리어답터 일 때 
            dp[num][1] += min(dp[i][1],dp[i][0])


solve_dp(1)
print(min(dp[1][0],dp[1][1]))