import heapq
def solution(food_times, k):
    answer = 0
    # 다 먹어버리는 경우 
    if sum(food_times) <= k : 
        return -1 
    h = [] 
    # 음식 수 , index로 삽입 
    for n,f in enumerate(food_times,1) : 
        heapq.heappush(h,(f,n))
    food_num =len(food_times)
    previous = 0
    
    # heap이 빌 때까지 
    while h  :
        t = (h[0][0]-previous) * food_num
        if t <= k : 
            k -= t 
            previous,a = heapq.heappop(h)
            food_num -= 1
        else : 
            idx = k % food_num
            h.sort(key = lambda x : x[1])
            answer = h[idx][1]
                
            break
            
            
        
        
            
                
            
            
    
    return answer