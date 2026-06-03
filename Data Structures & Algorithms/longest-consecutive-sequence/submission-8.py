class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        numSet = set(nums)

        for num in nums:
            if (num-1) not in numSet:
                lenght = 0

                while (num+lenght) in nums:
                    lenght +=1
                longest = max(longest,lenght)

        return longest