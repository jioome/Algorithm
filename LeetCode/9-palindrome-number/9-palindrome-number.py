class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        lst = [] 
        for i in str(x) :
            lst.append(i)
        if lst == lst[::-1]:
            return True
        return False
            
      