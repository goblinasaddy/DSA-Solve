class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        n = len(nums)
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue

            j=i+1
            k = n-1

            while j<k:
                summ = (nums[i]+nums[j]+nums[k])

                if summ<0: j+=1
                elif summ>0: k-=1

                else:
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1

        return list(res)