class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = s[0]
        if len(s) == 1 or s == s[::-1]: 
            return s
        for i in range(len(s)):
            prev = i-1
            after = i+1
            while True : 
                if prev >= 0 and after <len(s) and s[prev] == s[after]:
                    count = s[prev: after+1]
                    prev-= 1
                    after+=1
                elif i >= 0 and after <len(s) and s[i] == s[after]:
                    prev = i
                    count = s[prev: after+1]
                    prev-= 1
                    after+=1
                    
                else :
                    break
                if len(max_str) < len(count):
                    max_str = count
        return max_str
                    
                    
                    
            