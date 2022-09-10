def solution(info, edges):
    # 부모 노드 먼저 방문했나?
    # 자식 노드 방문한 적이 없나? 
    answer = [] 
    visited = [0]*len(info)
    visited[0] = 1 
    
    def dfs(sheep,wolf):
        if sheep > wolf:
            answer.append(sheep)
        else :
            return 
        for i in range(len(edges)):
            parent = edges[i][0]
            child = edges[i][1]
            iswolf = info[child]
            if visited[parent] == 1 and not visited[child]: 
                visited[child] = 1 
                if iswolf == 1 :
                    dfs(sheep,wolf+1)
                else :
                    dfs(sheep + 1 , wolf)
                visited[child] = 0 
        
        
        
    
    dfs(1,0)
    return max(answer)