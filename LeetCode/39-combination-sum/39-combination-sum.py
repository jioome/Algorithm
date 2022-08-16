class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(idx,lst):
            if target == sum(lst) : 
                
                result.append(lst)
                return 
                
            for i in range(idx,len(candidates)):
                
                if sum(lst)<= target : 
                    dfs(i,lst+[candidates[i]])
                
            
            
           
        dfs(0,[])
        return result
    