class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        dic = { ")":"(" , "}":"{", "]":"[" }
        for i in range(len(s)): 
            start = s[i]
            
            if start == ")" or  start == "]" or start == "}":

                if len(stack)>0 and stack[-1] == dic[start] :
                    stack.pop()
                else : 
                    stack.append(start)
                    
            else : 
                stack.append(s[i])
        if len(stack) == 0 : 
            return True
        else : 
            return False
                
            