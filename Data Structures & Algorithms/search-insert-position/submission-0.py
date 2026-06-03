class Solution:
    def lb(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,n-1
        ans = n

        while l<=r:
            mid = (l+r)//2

            if nums[mid]>= target:
                ans = mid
                r = mid-1

            else:
                l = mid+1

        return ans
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.lb(nums,target)