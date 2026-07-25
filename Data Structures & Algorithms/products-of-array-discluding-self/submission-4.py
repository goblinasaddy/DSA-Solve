class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prefix = 1
        postfix = 1

        for i in range(len(res)):
            res[i]=prefix
            prefix*=nums[i]

        for i in range(len(res)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]

        return res
# nums = [1,2,4,6]
# res = [1,1,1,1]

# prefix = 1
# for i = 0:
#     res = [1,1,1,1]
#     prefix = 1

# for i = 1:
#     res = [1,1,1,1]
#     prefix = 2
# for i = 2:
#     res = [1,1,2,1]
#     prefix = 8
# for i =3:
#     res = [1,1,2,8]
#     prefix = 48


# nums = [1,2,4,6]
# res = [1,1,2,8]

# postfix = 1
# for i = 3:
#     res = [1,1,2,8]
#     postfix = 6

# for i = 2:
#     res = [1,1,12,8]
#     postfix = 24

# for i = 1:
#     res = [1,24,12,8]
#     postfix = 48
# for i = 0:
#     res = [48,24,12,8]
#     postfix = 48


# return res

























