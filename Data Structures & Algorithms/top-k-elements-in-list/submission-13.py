class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        n = len(nums)
        bucket=[[] for _ in range(n+1)]

        for num,f in freq.items():
            bucket[f].append(num)

        res = []
        for i in range(n,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res





# freq = {1:1,
#         2:2,
#         3:3}

# bucket = [[1],[2],[3],[]]