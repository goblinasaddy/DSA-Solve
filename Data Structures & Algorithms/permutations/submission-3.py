class Solution:
    def backtrack(self,nums,path,used,result):
        if len(path)==len(nums):
            result.append(path.copy())
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            used[i]=True
            path.append(nums[i])
            self.backtrack(nums,path,used,result)
            path.pop()
            used[i]=False
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False]*len(nums)
        self.backtrack(nums,[],used,result)

        return result