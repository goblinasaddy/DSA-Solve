class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numC = Counter(nums)
        ans = []
        res = []

        for num,c in numC.items():
            ans.append([c,num])

        ans.sort()
        while len(res)<k:
            res.append(ans.pop()[1])

        return res