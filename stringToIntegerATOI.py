class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        out = ''
        memo = {
            ' ': 0,
            'mark': True,
            'num': True
        }
        mark = 1

        for c in s:
            if c == " " and memo['mark'] and memo['num']:
                continue

            elif (c == '+' or c == '-') and (memo['mark'] and memo['num']):
                mark = int(c+'1')
                memo['mark'] = False
                continue
            
            elif c.isdigit():
                memo['num'] = False
                out = out + c
            else: break

        if not out: return 0
        
        result = mark*int(out)
        if result> (2**31)-1:
            result = (2**31)-1
        elif result < (-2**31):
            result = -2**31

        return result
