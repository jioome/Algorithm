def solution(info, edges):
    
    answer = []
    visited = [0]*len(info)
    visited [0] = 1
    
    
    def dfs(sheep,wolf):
        if sheep <= wolf : 
            return 
        else : 
            answer.append(sheep)
            
        for p,c in edges : 
            iswolf = info[c]
            if visited[p] and not visited[c] : 
                visited[c] =1 
                if iswolf : 
                    dfs(sheep,wolf+1)
                else : 
                    dfs(sheep+1,wolf)
                visited[c] =0
                

            
                
            
    
    dfs(1,0)
    return max(answer)