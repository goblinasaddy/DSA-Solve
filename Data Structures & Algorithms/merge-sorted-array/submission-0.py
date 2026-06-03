class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m
        j = 0
        n = len(nums1)

        while i<n:
            if nums1[i]==0:
                nums1[i],nums2[j]=nums2[j],nums1[i]
                i+=1
                j+=1

        return nums1.sort()
        