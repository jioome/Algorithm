import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())

# root 노드 찾기
def find(x):
    if parent[x] != x : 
        parent[x] = find(parent[x])
        return parent[x]
    else : 
        return x

# root 노드 합치기 
def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y :
        parent[root_y] = root_x
        number[root_x]+= number[root_y]
        

for i in range(n):
    parent = dict()
    number = dict()
    f = int(input())
    for j in range(f):
        x,y = input().split()
        # 자기 자신 부모로 초기화 
        if x not in parent : 
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y 
            number[y] = 1
        
        union(x,y)
        print(number[find(x)])