class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for i in range(len(nums)):
            if (nums[i]-1) not in numSet:
                lenght =0

                while (nums[i]+lenght) in nums:
                    lenght +=1

                longest = max(longest,lenght)

        return longest
