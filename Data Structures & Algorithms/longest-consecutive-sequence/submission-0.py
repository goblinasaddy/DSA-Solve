class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in set1:
                lenght = 0
                while (n+lenght) in set1:
                    lenght +=1
                longest = max(longest,lenght)

        return longest
