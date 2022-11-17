import sys
input = sys.stdin.readline 
n,m = map(int,input().split())

# lst = [i for i in range(1,n+1)]
lst = [] 
def dfs(start):
    if len(lst) == m : 
        print(*lst)
    for i in range(start,n+1):
        if i not in lst : 
            lst.append(i)
            dfs(i)
            lst.pop()

dfs(1)
