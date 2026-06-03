class Solution:
    def solve(self,start,nums,subset,result):
        result.append(subset.copy())

        for i in range(start,len(nums)):
            if i>start and nums[i]==nums[i-1]:
                continue

            subset.append(nums[i])
            self.solve(i+1,nums,subset,result)
            subset.pop()
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        self.solve(0,nums,[],result)
        return result