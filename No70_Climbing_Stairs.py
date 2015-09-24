#No.70_Climbing_Stairs
#You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#走完n个台阶的方式有f(n)种。而走完n个台阶有两种方法，先走完n-2个台阶，然后跨2个台阶；先走完n-1个台阶，然后跨1个台阶。
#所以f(n) = f(n-1) + f(n-2)。
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        dp = [1 for i in range(n+1)]
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]