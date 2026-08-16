class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canship(cap):
            d=1
            curr=0
            for w in weights:
                if curr+w>cap:
                    d+=1
                    curr=0
                curr+=w
            return d<=days

        left=max(weights)
        right=sum(weights)

        while left<right:
            mid=(left+right)//2

            if canship(mid):
                right=mid
            else:
                left= mid+1
        return left