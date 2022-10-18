class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = [] 
        def dfs(k,lst,idx):
            if k == 0 : 
                result.append(lst[:])
                return 
            for i in range(idx,n+1):
                dfs(k-1,lst+[i],i+1)
        
        dfs(k,[],1)
        
        return result