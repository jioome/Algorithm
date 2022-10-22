class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = bin(x^y).count('1')
        print(result)
        return result