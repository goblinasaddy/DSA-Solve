class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        summ = 0
        ans = 15000000
        i = 0
        for j in range(n):
            summ += nums[j]
            while summ >= target:
                ans = min(ans,(j-i+1))
                summ -= nums[i]
                i+=1

        if ans == 15000000:
            return 0
        return ans        