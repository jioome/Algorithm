# 거쳐가는 정점을 기준으로 최단 거리를 구하는 것 
# Floyd-Warshall 알고리즘이란, 위 경우에서 마지막에 해당하는 모든 최단 경로를 구하는 방법 입니다.
import sys
input = sys.stdin.readline 
n = int(input())
m = int(input())
graph = [[float('inf')]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    if graph[a][b] > c : 
        graph[a][b] = c

# 자기 자신은 0 
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j : 
            graph[i][j] = 0 

# floyd warshall 
# x 를 반복문 마지막에 돌리니까 이상해짐
for x in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][x] + graph[x][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == float('inf'):
            print(0,end = ' ')
        else : 
            print(graph[i][j],end = ' ')
    print()

