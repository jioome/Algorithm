class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(target,idx,lst):
            if target == sum(lst) : 
                
                result.append(lst)
                return 
                
            for i in range(idx,len(candidates)):
                
                if sum(lst)<= target : 
                    dfs(target,i,lst+[candidates[i]])
                
            
            
           
        dfs(target,0,[])
        return result
    