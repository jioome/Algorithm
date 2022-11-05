import sys
input = sys.stdin.readline
'''
모든 도시에서 모든 도시로 가는 최소 비용 
n3
플로이드 

'''
n= int(input())
m = int(input())
inf = float('inf')
dist = [[inf]*(n+1) for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    dist[a][b] = min(dist[a][b],c)
for i in range(n+1):
    for j in range(n+1):
        if i == j : 
            dist[i][j] = 0
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if dist[i][j] == inf : 
            print(0,end = ' ')

        else : 
            print(dist[i][j],end = ' ')
        
    print()