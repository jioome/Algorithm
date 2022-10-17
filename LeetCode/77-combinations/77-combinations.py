class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def dfs(lst,idx,k):
            if k == 0 : 
                result.append(lst[:])
                return 
            for i in range(idx,n+1):
                lst.append(i)
                dfs(lst,i+1,k-1)
                lst.pop()
                
        
        dfs([],1,k)
        return result
        