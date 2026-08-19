from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows=defaultdict(int)

        #shift the bitmask
        for r,s in reservedSeats:
            rows[r]|=1<<s
        
        ans=(n-len(rows))*2

        left  = (1<<2) | (1<<3) | (1<<4) | (1<<5)
        middle= (1<<4) | (1<<5) | (1<<6) | (1<<7)
        right=  (1<<6) | (1<<7) | (1<<8) | (1<<9)

        for map in rows.values():
            left_free=(map&left)==0
            middle_free=(map&middle)==0
            right_free=(map&right)==0

            if left_free and right_free:
                ans+=2
            elif left_free or middle_free or right_free:
                ans+=1
        return ans
