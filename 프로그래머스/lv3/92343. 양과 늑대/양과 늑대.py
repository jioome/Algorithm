def solution(info, edges):
    
    answer = [] 
    visited = [0]*(len(info))
    visited[0] = 1 
    
    
    def dfs(sheep,wolf):
        if sheep <= wolf:
            return 
        answer.append(sheep)
        
        for p,c in edges:
            if visited[p] == 1 and visited[c] == 0 : 
                visited[c] =1
                iswolf = info[c]
                if iswolf : 
                    dfs(sheep,wolf+1)
                else : 
                    dfs(sheep+1,wolf)
                visited[c] = 0 
            
                
            
    
    dfs(1,0)
    return max(answer)