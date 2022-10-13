import sys 
from collections import deque
input = sys.stdin.readline
n = int(input())
building = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
cost= [0]*(n+1)

for i in range(1,n+1):
    data = list(map(int,input().split()))[:-1]
    cost[i] = data[0]
    building_data= data[1:]

    for j in building_data:
        # 그래프 그리기 
        building[j].append(i)
        indegree[i] += 1

# 위상정렬
def topology():
    # 선수 건물 짓는데 걸리는 시간 
    result = [0] * (n + 1)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result[now] += cost[now]

        for b in building[now]:
            # 선수 빌딩 짓는 시간 5,10 -> 큰게 최소
            result[b] = max(result[now],result[b])
            indegree[b] -= 1 
            if indegree[b] == 0 : 
                q.append(b)
        

    return result
answer = topology()
for i in range(1,n+1):
    print(answer[i])

    