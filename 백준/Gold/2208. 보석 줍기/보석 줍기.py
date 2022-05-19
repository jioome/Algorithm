import sys

# dp[i] = max(dp[i-1] + arr[i], pre[i] - pre[i-M])

input = sys.stdin.readline 
n,m = map(int,input().split())
prefix_sum = [0] # 구간합 
arr = [0] * n 
value = 0 
for i in range(n):
    arr[i] = int(input())
    value += arr[i]
    prefix_sum.append(value)
ans , tmp = 0,0
for i in range(m-1,n):
    # M - 1 부터 확인하는 이유는 M - 1 보다 작을 경우 길이 M 이상인 부분 배열을 고를 수 없기 때문
    tmp = min(tmp,prefix_sum[i-(m-1)]) 
    ans = max(ans,prefix_sum[i+1]-tmp)
print(ans)
    

