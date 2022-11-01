'''
bfs연결 되 있는 것  
graph 그리기 
연결된 컴퓨터 수 찾기 
'''
import sys 
from collections import deque
input = sys.stdin.readline 
n=int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(a) :
    visited[a] = 1
    q = deque()
    q.append(a)
    cnt = 0 
    while q :
        x =q.popleft()
        for i in graph[x]:
            if visited[i] == 0: 
                visited[i] = 1
                cnt += 1 
                q.append(i)
    return cnt 

print(bfs(1))
