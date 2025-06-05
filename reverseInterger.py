class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        out = x
        if x<0: out = out*(-1)
        out = str(out)
        out = int(out[::-1])
        out = int(out)
        if x<0: out = out*(-1)
        if out <= (-2)**31 or out >= (2**31)-1: return 0
        return out
        
