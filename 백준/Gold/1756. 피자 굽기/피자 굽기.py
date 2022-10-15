import sys 

# 오븐 깊이 , 반죽 개수
d,n = map(int,input().split())
# 오븐 지름 
oven = list(map(int,input().split()))
# 피자 지름 
doughs = list(map(int,input().split()))

for i in range(1,len(oven)):
    if oven[i]>oven[i-1]:
        oven[i] = oven[i-1]

# 도우가 어디에 쌓이는지
pile_d = 0 
l = 0 
r = len(oven)-1
for d in doughs:
    is_pile = False
    while l <= r : 
        mid = (l + r)// 2 
        diameter = oven[mid]
        
        if diameter >= d :
            l = mid + 1
            is_pile = True
            pile_d = mid
        else :
            r = mid-1

    if not is_pile:
        pile_d -= 1
        break
    l = 0 
    r = pile_d-1

if pile_d == -1 : 
    print(0)
else : 
    # 반죽의 
    print(pile_d+1)
 
