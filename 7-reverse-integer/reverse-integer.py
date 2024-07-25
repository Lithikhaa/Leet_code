class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        
        reversed = int(str(x)[::-1])
        if reversed > 2**31 - 1:
            return 0

        return sign * reversed
        

        
# 1 * 120 --> 12
# -1 * 123 --> -321

