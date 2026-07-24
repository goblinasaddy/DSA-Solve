class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp not in hm:
                hm[num]=i
            else:
                return [hm[comp],i]