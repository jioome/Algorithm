class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = [] 
        arr = [i for i in range(n+1)]
        def dfs(idx,k,lst):
            if k == 0 : 
                answer.append(lst[:])
            for i in range(idx,n+1):
                lst.append(i)
                dfs(i+1,k-1,lst)
                lst.pop()
                
            
            
        dfs(1,k,[])
        print(answer)
        return answer