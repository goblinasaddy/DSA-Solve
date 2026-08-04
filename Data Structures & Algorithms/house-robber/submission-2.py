class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def solve(index):

            if index==0:
                return nums[index]

            if index<0:
                return 0

            pick = nums[index]+solve(index-2)
            not_pick = 0 + solve(index-1)

            return max(pick,not_pick)

        return solve(n-1)