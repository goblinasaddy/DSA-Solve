class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = Counter(nums)
        print(hashmap)
        for num in hashmap:
            if hashmap[num]>1:
                return True

        return False