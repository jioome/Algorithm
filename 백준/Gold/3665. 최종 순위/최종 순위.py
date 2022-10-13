from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    # 작년 순위
    n = int(input())
    rank = list(map(int,input().split()))
    indegree = [-1] + [0]*n
    graph = [[] for _ in range(n+1)]
    for i in range(n):
        graph[rank[i]] = rank[i+1:]
        indegree[rank[i]] = i
    
    # 순위 역전
    for _ in range(int(input())):
        a,b = map(int,input().split())
        # 관계를 뒤집음 / 순위 뒤집는게 아니라 관계에 초점 
        # 두 갈래로 분기
        if a in graph[b]:
            graph[b].remove(a)
            graph[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1
        else:
            graph[a].remove(b)
            graph[b].append(a)
            indegree[b] -= 1
            indegree[a] += 1
            
    # 시작 노드
    q = deque()
    for i in range(1,n+1):
        if not indegree[i]:
            q.append(i)
    if not q:
        # 시작 노드 부재, 사이클
        print("IMPOSSIBLE")
        continue
    
    # 위상 정렬
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for i in graph[v]:
            indegree[i] -= 1
            if not indegree[i]:
                q.append(i)
    if len(ans)!= n:
        # 사이클 존재
        print("IMPOSSIBLE")
    else:
        print(*ans)
