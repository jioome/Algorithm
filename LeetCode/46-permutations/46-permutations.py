class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = [] 
        lst = [] 
        def dfs(elements):
            if len(elements) == 0 :
                answer.append(lst[:])
            
           
            for e in elements:
                nxt = elements[:]
                lst.append(e)
                nxt.remove(e)
                dfs(nxt)
                lst.pop()
                
                
        dfs(nums)
        return answer
        