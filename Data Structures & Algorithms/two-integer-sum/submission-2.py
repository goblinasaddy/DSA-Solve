class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,num in enumerate(nums):
            rem = target - num

            if rem not in hashmap:
                hashmap[num] = i
            else:
                return [hashmap[rem], i]