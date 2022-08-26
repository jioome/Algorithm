
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort()
        for t in tickets:
            graph[t[0]].append(t[1])
        route = [] 
        def dfs(start):

            while graph[start] :
                dfs(graph[start].pop(0))
                
            route.append(start)

            
            
            
        
        dfs("JFK")

        return route[::-1]