class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounter = Counter(nums)
        ans = []

        for num,c in numCounter.items():
            ans.append([c,num])

        ans.sort()
        res = []
        while len(res)<k:
            res.append(ans.pop()[1])

        return res