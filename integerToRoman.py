class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = {
            1: 'I',
            5: "V",
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',

        }
        #499 
        power = len(str(num))-1
        out = ''
        for c in str(num):
            lvl = 10**power

            if c == '4':
                out = out + roman[lvl]
                out = out + roman[5*lvl]
            elif c == '9':
                out = out + roman[lvl]
                out = out + roman[10*lvl]
            elif int(c)>=5 and int(c)<9:
                out = out + roman[5*lvl]
                out = out + (int(c)-5)*roman[lvl]
            elif int(c)<4 and int(c)>0:
                out = out + int(c)*roman[lvl]
            power = power - 1

        return out
