def solution(stones, k):
    '''
    건너 뛸 수 있는 수 k
    
    
    '''
    left = 0 
    right = 200000000
    while left <= right : 
        # 친구 수 
        mid = (left + right) // 2
        cnt = 0 
        for s in stones : 
            if s -mid <= 0 : 
                cnt += 1 
                if cnt >= k : 
                    break
            else : 
                cnt = 0 
        if cnt < k  :
            left = mid + 1
        elif cnt >= k  : 
            right = mid - 1

    
    return left