import sys

n = int(input())
homework =[]
visited = [0] * 1001
for _ in range(n):
    d,w = map(int,input().split())
    homework.append([d,w])

homework.sort(key=lambda x : x[1],reverse=True)
answer =0 

for day, worth in homework:
    i = day
    # 과제를 할 날짜 탐색
    while i > 0 and visited[i]:
        i -= 1
    # 과제를 할 날짜가 없으면 패스
    if i == 0:
        continue
    else:
        visited[i] = True # 과제 완료 
        answer += worth # 점수를 더해준다. 

print(answer)

