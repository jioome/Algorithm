import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline 

n = int(input())
graph= [[] for _ in range(n+1)]
visited = [0]*(n+1)


# 인접 x , 양방향 
cost = [0] + list(map(int,input().split()))
dp= [[0,cost[i]] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(cur):
    visited[cur] = 1 
    for u in graph[cur]:
        if not visited[u]:
            dfs(u)
            dp[cur][1] += dp[u][0]
            dp[cur][0] += max(dp[u][0],dp[u][1])

dfs(1)
print(max(dp[1][1],dp[1][0]))


