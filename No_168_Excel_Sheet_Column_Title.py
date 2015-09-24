#No.168_Excel_Sheet_Column_Title
#Given a positive integer, return its corresponding column title as appear in an Excel sheet.

class Solution:
    # @return a string
    def convertToTitle(self, num):
        alpha = [chr(i) for i in range(65,91)]
        res = []
        while num > 0:
            t = num % 26
            print t
            res.append(alpha[t-1])
            num = (num / 26)
            if t == 0:
                num -= 1
        return ''.join(res[::-1])

s = Solution()
print s.convertToTitle(52)