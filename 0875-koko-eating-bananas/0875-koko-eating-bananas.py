class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<r:
            mid=(l+r)//2
            hr=0
            for pile in piles:
                hr+=(pile+mid-1)//mid
            if hr<=h:
                r=mid
            else:
                l=mid+1
        return l

        