def solution(tickets):
    route = {}

    for t in tickets : 
        s = t[0]
        a = t[1] 
        route[s] = route.get(s,[])+[a]
    for r in route : 
        route[r].sort(reverse=True)
    stack =["ICN"]
    path = [] 
    while stack : 
        tmp = stack[-1]
        if tmp not in route or len(route[tmp]) == 0 : 
            path.append(stack.pop())
        else : 
            stack.append(route[tmp][-1])
            route[tmp] = route[tmp][:-1]
            
        
    return path[::-1]