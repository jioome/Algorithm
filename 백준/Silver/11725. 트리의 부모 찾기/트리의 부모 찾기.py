
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline 
n = int(input())
tree = [[]for _ in range(n+1)]

for i in range(1,n):
    a,b = map(int,input().split())
    tree[a].append(b) # 두 개 다 연결되어 있는 
    tree[b].append(a)

par = [-1]*(n+1)
def dfs(n):
    for i in tree[n] : 
        if par[i] == -1 : 
            par[i] = n 
            dfs(i)




dfs(1)
for i in range(2,n+1):
    print(par[i])
