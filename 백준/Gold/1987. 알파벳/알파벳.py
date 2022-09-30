import sys
from collections import deque
input=sys.stdin.readline

R,C=map(int,input().split())
arr=[list(input()) for _ in range(R)]
check=[['']*C for _ in range(R)]
l=[(0,0,1,arr[0][0])]
MAX=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]
while l:
    x,y,cnt,total=l.pop()
    if MAX<cnt:
        MAX=cnt
    if MAX==26:
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<R and 0<=ny<C:
            if arr[nx][ny] not in total:
                temp=total+arr[nx][ny]
                if check[nx][ny]!=temp:
                    check[nx][ny]=temp
                #print(check,l)
                    l.append((nx,ny,cnt+1,temp))
print(MAX)
    