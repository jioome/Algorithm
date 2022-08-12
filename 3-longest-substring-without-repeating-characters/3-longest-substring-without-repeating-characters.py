from collections import *
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        use = [] 
        for i in s:
            if i not in use :
                use.append(i)
                max_length = max(max_length,len(use))
            else :  
                use = use[use.index(i)+1 :][:]
                use.append(i)
                max_length = max(max_length,len(use))
        return max_length 
       