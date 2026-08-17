class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        ans =0
        length = 0

        for i in range(len(nums)):
            if (nums[i]-1) not in numset:
                length = 1

                while (nums[i]+length) in numset:
                    length +=1
                ans = max(ans,length)

        return ans

