class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r

        while l<=r:
            k = (l+r)//2
            hour = 0

            for pile in piles:
                hour += (pile + k -1)//k

            if hour <= h:
                ans = k
                r = k-1
            else:
                l = k+1

        return ans