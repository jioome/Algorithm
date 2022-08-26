class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = [] 
        path = [] 
        def dfs(idx,n,k):
            if k == 0  : 
                result.append(path[:])
                return 

            for i in range(idx,n):
                path.append(i+1)
                dfs(i+1,n,k-1)
                path.pop()

        dfs(0,n,k)

        return result 