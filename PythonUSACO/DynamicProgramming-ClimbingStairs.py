class Solution:
    def climbStairs(self, n: int) -> int:
        #@cache
        def ClimbRecur(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            return ClimbRecur(n - 1) + ClimbRecur(n - 2)

        return ClimbRecur(n)


