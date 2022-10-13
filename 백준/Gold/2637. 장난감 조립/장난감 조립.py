import sys 
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
graph  =[[] for _ in range(n+1)]
# 제품 만들 때 필요한 부품 
needs = [[0]*(n+1) for _ in range(n+1)]
q = deque()
indegree = [0]*(n+1)

for i in range(m):
    x,y,k = map(int,input().split())
    graph[y].append((x,k))
    indegree[x] += 1
for i in range(1,n+1):
    if indegree[i] == 0 : 
        q.append(i)
while q :
    now = q.popleft()
    # 현 제품의 다음 단계 번호, 현 제품이 얼마나 필요한지
    for next,next_need in graph[now]:
        # 현 제품이 기본 부품이면
        if needs[now].count(0) == n+1:
            # 다음 부품 개수 구하기 
            needs[next][now] += next_need
        else : 
            # 현 제품이 중간 제품이면
            for i in range(1,n+1):
                # next= 7 i= 1 now = 5 i = 1 needs = 2
                # 5번 중간 부품 만드는데 1번 부품 2개 필요
                # 7번 만드는데 5번 중간 부품 2개 필요  -> 총 2*2
                needs[next][i] += needs[now][i]*next_need
        indegree[next] -= 1
        if indegree[next] == 0 : 
            q.append(next)
for x in enumerate(needs[n]):
    if x[1]>0 : 
        print(*x)






