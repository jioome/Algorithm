from collections import *
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = [] 
        dic = defaultdict(list)
        for t in tickets : 
            dic[t[0]].append(t[1])
            
        for d in dic : 
            dic[d].sort(reverse=True)
        def dfs(start) : 
            while dic[start] : 
                next = dic[start].pop()
                dfs(next)
            result.append(start)
            
            
        
        dfs("JFK")
        return result[::-1]
