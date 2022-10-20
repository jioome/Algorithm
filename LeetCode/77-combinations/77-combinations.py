class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(n+1)]
        result = [] 
        def dfs(idx,k,lst):
            if k == 0 :
                result.append(lst)
            for i in range(idx,n+1):
                dfs(i+1,k-1,lst+[arr[i]])
            
        dfs(1,k,[])
        return result
        