import sys

input = sys.stdin.readline 
t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))
    dp = array[:] # deep copy 1차원 배열만 가능 
    for i in range(1,n):
        dp[i] = max(array[i]+dp[i-1],array[i])

    print(max(dp))

