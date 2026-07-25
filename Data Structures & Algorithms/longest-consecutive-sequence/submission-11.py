class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long = 0
        numSet = set(nums)

        for num in nums:
            if (num-1) not in numSet:
                length = 0

                while (num + length) in nums:
                    length +=1
                    long = max(long,length)

        return long
