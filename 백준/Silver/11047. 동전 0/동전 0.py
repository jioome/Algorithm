import sys
input = sys.stdin.readline 
n,k  = map(int,input().split())
money = []
cnt = 0 
for _ in range(n):
    money.append(int(input()))

money.sort(reverse=True) # 큰 동전부터 뽑아준다
 
for m in money : 
    if m <= k :
        cnt += (k // m)
        k -= (k // m)*m
    if k == 0 : 
        break

print(cnt) 

