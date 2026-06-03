class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maxCount =res=0

        for num,f in freq.items():
            if maxCount < f:
                res = num
                maxCount = f
        return res
        






            