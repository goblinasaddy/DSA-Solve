class Solution:
    def solve(self,index,total, nums, target, subset,result):
        if total==target:
            result.append(subset.copy())
            return 
        elif total>target:
            return
        if index>=len(nums):
            return
        summ = total+nums[index]
        subset.append(nums[index])
        self.solve(index,summ,nums,target,subset,result)
        summ = total
        subset.pop()
        self.solve(index+1,summ,nums,target,subset,result)
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(0,0,nums,target,[],result)
        return result