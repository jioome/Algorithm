from collections import deque
def solution(cacheSize, cities):
    answer = 0
    city = [] 
    buffer = deque()
    
    if cacheSize == 0 : 
        return len(cities) * 5
    for c in cities : 
        c = c.lower()
        if c in buffer : 
            answer += 1
        else : 
            answer += 5
        
        if c in buffer : 
            buffer.remove(c)
            buffer.append(c)
            continue 
        elif len(buffer)>=cacheSize :
            buffer.popleft()
            buffer.append(c)
        else:
            buffer.append(c)
        
    
    
    return answer