#No231_Power_of_Two
#如果一个整数是2的幂，那么它的二进制形式最高位为1，其余各位为0
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n > 0 and n & (n - 1) == 0

