from itertools import *
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = [] 
        dic = {"2":'abc',"3":'def',"4":'ghi',"5":'jkl',"6":'mno',"7":'pqrs',"8":'tuv',"9":'wxyz'}
        if len(digits) == 0 : 
            return [] 
        def dfs(idx,path) : 
            if len(path) == len(digits) : 
                result.append(path)
                return 
            for i in range(idx,len(digits)) : 
                for j in dic[digits[i]]:
                    dfs(i+1, path + j)

        dfs(0,'')
            
            
                
        return result
            