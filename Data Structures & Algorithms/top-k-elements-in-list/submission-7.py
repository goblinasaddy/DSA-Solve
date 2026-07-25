class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        arr=[]
        for num,c in freq.items():
            arr.append([c,num])

        arr.sort()

        res = []
        while len(res)<k:
            res.append(arr.pop()[1])

        return res
