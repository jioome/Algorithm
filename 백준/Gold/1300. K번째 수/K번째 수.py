
import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

start, end = 0, k # k번째 수는 k보다 클 수 없음

while start <= end:
    mid = (start+end) // 2
    cnt = 0

    for i in range(1,n+1):
        cnt += min(mid//i, n)  # n x n 에서 mid 보다 작거나 같은 수
    
    if cnt >= k: # k 번째로 오는 수를 찾는다 
        end = mid - 1
    else:
        start = mid + 1

print(start)