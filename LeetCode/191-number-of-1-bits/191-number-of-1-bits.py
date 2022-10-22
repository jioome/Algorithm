class Solution:
    def hammingWeight(self, n: int) -> int:
        result  = bin(n).count('1')
        return result
        