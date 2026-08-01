from collections import Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr1=Counter(nums1)
        arr2=Counter(nums2)
        ans=[]

        for ch in nums1:

            if ch in nums2:
                ans.append(ch)

        ans1=set(ans)

        return list(ans1)


        