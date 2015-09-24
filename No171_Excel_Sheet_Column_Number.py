#No.171_Excel_Sheet_Column_Number
#Given a column title as appear in an Excel sheet, return its corresponding column number.
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        res = 0
        l = len(s)
        for i in range(l):
            res *= 26
            res += ord(s[i]) - 64
        return res


print Solution().titleToNumber('Z')        