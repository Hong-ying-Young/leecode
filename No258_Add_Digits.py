#Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
class Solution:
    def addDigits(self,num):
        while num > 9:
            a = 0
            a = num % 10
            num /= 10
            b = a + num   
            num = b
        return num

#test
x = Solution()
x.addDigits(25)