import heapq
def solution(scoville, k):
    '''
    스코빌 가장 낮은 두 개 
    젤작 + 두번째 작 *2
    '''
    heapq.heapify(scoville)
    cnt = 0 
    while True : 
        if len(scoville) == 1 and scoville[0] < k : 
            return -1
            
        s = heapq.heappop(scoville)
        if s>= k : 
            break
        if s <k : 
            cnt += 1
            s2 = heapq.heappop(scoville)
            new = s + s2*2
            heapq.heappush(scoville,new)
    

    
    return cnt