import sys

input = sys.stdin.readline 
N = int(input())
time = []

for _ in range(N):
  time.append(list(map(int,input().split())))

time.sort() # 시작 시간을 기준으로 오름차순
time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순

last = 0 # 회의의 마지막 시간
cnt = 0 # 회의 개수

for i, j in time:
  if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    cnt += 1
    last = j

print(cnt)