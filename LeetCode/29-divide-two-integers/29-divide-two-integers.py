class Solution:
     def divide(self, dividend: int, divisor: int) -> int:
        sign = 1 
        if dividend == 0:
            return 0
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        if dividend * divisor < 0:
            sign = -1
            
        quotient = 0 
        dividend = abs(dividend)
        divisor = abs(divisor)
            
        while dividend-divisor  >= 0 : 
            x = 0
            while dividend - (divisor<< x)>=0:
                x += 1
            dividend = dividend - (divisor << x-1)

            quotient += 2**(x-1)

        return quotient if sign== 1 else -quotient
            
            
            
            

        