class Solution:
    def isRectangleOverlap(self, rec1, rec2):

        if rec1[2] <= rec2[0]:   # rec1 left of rec2
            return False

        if rec2[2] <= rec1[0]:   # rec2 left of rec1
            return False

        if rec1[3] <= rec2[1]:   # rec1 below rec2
            return False

        if rec2[3] <= rec1[1]:   # rec2 below rec1
            return False

        return True
        