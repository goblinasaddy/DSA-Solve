class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        set1 = set(nums)

        for num in nums:
            if (num-1) not in set1:
                lenght = 0

                while (num + lenght) in nums:
                    lenght +=1
                longest = max(lenght , longest)
        return longest