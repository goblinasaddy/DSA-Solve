class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        val = n/3

        freq = Counter(nums)
        max_occ = 0
        res = []
        for num,f in freq.items():
            if f>val:
                max_occ = f
                res.append(num)
        return res
