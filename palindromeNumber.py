class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        r = str(x)
        l = r[::-1]
        if r==l: return True
        return False
