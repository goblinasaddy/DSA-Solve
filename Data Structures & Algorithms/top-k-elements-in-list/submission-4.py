class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(num for num,_ in Counter(nums).most_common(k))