class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounter = Counter(nums)
        arr = []
        for num,c in numCounter.items():
            arr.append([c,num])

        arr.sort()

        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])

        return res
        

