class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        maxV = 0
        temp = ""
        
        while True:
            temp = ''
            for c in s:
                if c not in temp:
                    temp += c
                    maxV= len(temp) if len(temp)>maxV else maxV
                else: 
                    s = s[1:]
                    break

            else: break

        return maxV
