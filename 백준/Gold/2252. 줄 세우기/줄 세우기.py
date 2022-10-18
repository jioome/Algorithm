import sys
from collections import deque
input = sys.stdin.readline
q = deque()
n,m = map(int,input().split())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
answer = [] 
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] +=1

for i in range(1,n+1):
    if indegree[i] == 0 : 
        q.append(i)
    
while q : 
    cur = q.popleft()
    answer.append(cur)
    for i in graph[cur]:
        indegree[i]-=1
        if indegree[i] == 0 : 
            q.append(i)
print(*answer)
