class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
            
        result = []
        
        def dfs(idx,lst):
            
            if len(lst) == k:
                result.append(lst)
            
            for i in range(idx+1,n+1):
                dfs(i,lst+[i])
                if i+k >n :
                    continue
                
        for i in range(1,n+1):
            if k == 1 : 
                result.append([i])
            else : 
                dfs(i,[i])
        return result