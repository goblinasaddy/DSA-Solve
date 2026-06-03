class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] +=1
        n = len(nums)

        bucket = [[] for _ in range(n+1)]

        for num,f in freq.items():
            bucket[f].append(num)

        res = []
        for i in range(n,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
