import sys 
input = sys.stdin.readline
n,m  = map(int,input().split())
parent = dict()

def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_y] = parent[root_x]




for i in range(m):
    oper,a,b = map(int,input().split())
    if a not in parent:
        parent[a] = a
    if b not in parent:
        parent[b] = b
    if oper == 0 :
        union(a,b)
        
    else : 
        if find(a) == find(b):
            print("YES")
        else : 
            print("NO")