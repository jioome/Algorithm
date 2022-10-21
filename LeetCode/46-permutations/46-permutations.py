class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer =[] 
        lst = [] 
        def dfs(element):
            if not element : 
                answer.append(lst[:])
            for e in element:
                nxt = element[:]
                nxt.remove(e)
                lst.append(e)
                dfs(nxt)
                lst.pop()
                
        dfs(nums)
        return answer
        