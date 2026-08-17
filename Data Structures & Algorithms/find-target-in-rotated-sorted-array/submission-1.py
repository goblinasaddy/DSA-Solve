class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return next((n for n in range(len(nums)) if nums[n] == target), -1)

            