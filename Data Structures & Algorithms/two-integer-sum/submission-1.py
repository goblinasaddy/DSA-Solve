class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,num in enumerate(nums):
            comp = target - num
            if comp not in hashmap:
                hashmap[num] =i

            else:
                return [hashmap[comp],i]