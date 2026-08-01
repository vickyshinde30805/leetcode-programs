from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        arr1=Counter(nums1)
        arr2=Counter(nums2)
        for ch in arr1:
            if ch in arr2:
                ans1=min(arr1[ch],arr2[ch])
                ans.extend([ch]*ans1)

        return ans