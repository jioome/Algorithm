from collections import *
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = [] 
        dic = defaultdict(list)
        
        for t in tickets : 
            dic[t[0]].append(t[1])
        
        for d in dic : 
            dic[d].sort()
        def dfs(start):
            while dic[start]:
                a = dic[start].pop(0)
                dfs(a)
            result.append(start)
            
                
            
            
        dfs("JFK")
        return result[::-1]
