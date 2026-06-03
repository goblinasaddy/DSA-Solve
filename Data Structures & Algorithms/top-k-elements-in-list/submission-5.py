class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = Counter(nums)
        bucket = [[] for _ in range(n+1)]

        for num, f in freq.items():
            bucket[f].append(num)

        res = []
        for i in range(n,-1,-1):
            for num in bucket[i]:
                res.append(num)
            if len(res)==k:
                return res