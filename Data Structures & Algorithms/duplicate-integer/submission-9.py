class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_c = Counter(nums)

        for i in nums_c.values():
            if i>1:
                return True

        return False