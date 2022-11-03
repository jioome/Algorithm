from glob import glob
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

answer = [i for i in range(1,n+1)]
def dfs(i):
    if len(result) == m : 
        print(*result)
        return 
    for a in answer :
        if visited[a] == 0 :
            result.append(a)
            visited[a] = 1
            dfs(a)
            result.remove(a)
            visited[a] = 0 
    
    
for i in range(1,n+1):
    visited = [0]*(n+1)
    visited[i] = 1
    result = []
    result.append(i)
    dfs(i)
