class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev2 = prev = 1

        for curr in range(2,n+1):
            curr = prev2+prev
            prev2 = prev
            prev = curr

        return prev
        