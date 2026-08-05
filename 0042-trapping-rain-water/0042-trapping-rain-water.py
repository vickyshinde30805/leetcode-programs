class Solution:
    def trap(self, h: List[int]) -> int:
        n=len(h)
        l,r=0,n-1
        l_mx,r_mx=h[l],h[r]
        water=0

        while l<r:
            if l_mx < r_mx:
                l+=1
                l_mx=max(l_mx,h[l])
                water+=l_mx-h[l]
            
            else:
                r-=1
                r_mx=max(r_mx,h[r])
                water+=r_mx-h[r]
            
        return water

        
        
        