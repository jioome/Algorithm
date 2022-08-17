class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        trace = set() 
        visited = set()
        r = set()
        graph = defaultdict(list)
        for p in prerequisites :
            graph[p[1]].append(p[0])
        def dfs(start): 
            if start in visited : 
                return True 
            if start in trace : 
                return False 
            trace.add(start)
            
            for g in graph[start] : 
                if not dfs(g) : 
                    return False 
                
            trace.remove(start)
            visited.add(start)
            return True 
            
        
        for i in prerequisites :
            if not dfs(i[0]):
                return False 
            
        
        return True
            

        
            