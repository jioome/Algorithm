from itertools import *
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = [] 
        dic = {"2":'abc',"3":'def',"4":'ghi',"5":'jkl',"6":'mno',"7":'pqrs',"8":'tuv',"9":'wxyz'}
        if digits == '' : 
            return [] 
        def dfs(idx,word) : 
            if len(word) == len(digits) :
                result.append(word)
                return 
            
            for j in dic[digits[idx]]:
                dfs(idx+1,word + j )
    
        dfs(0,'')
        return result
            