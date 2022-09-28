from itertools import combinations

n, m = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(n)]
house = []
chicken = [] 
chicken_dis = []

# 치킨, 집 거리 표현
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i,j))
        if city[i][j] == 1:
            house.append((i,j))

result = float('inf') 
# 치킨집 m개 선택 경우의 수 모두 구함
com_chicken = list(combinations(chicken,m))

for com in com_chicken:
    distance = 0  
    # 집의 치킨 거리 구하기 
    for i,j in house : 
        chi_dis = float('inf')
        for a,b in com :
            chi_dis = min(abs(a-i) + abs(b-j),chi_dis)
        distance+= chi_dis
    result = min(result,distance)
 
print(result)