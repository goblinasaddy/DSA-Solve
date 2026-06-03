class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = Counter(nums)

        for num,f in freq.items():
            if f>1:
                return num

                