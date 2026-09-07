class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1=[]
        st2=[]

        for ch1 in s:
            if ch1!="#":
                st1.append(ch1)
            else:
                if st1:
                    st1.pop()
        
        for ch2 in t:
            if ch2!="#":
                st2.append(ch2)
            else:
                if st2:
                    st2.pop()
        
        return st1==st2
        