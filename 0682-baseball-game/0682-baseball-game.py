class stack:
    def __init__(self):
        self.val=[]
    def push(self,x):
        self.val.append(x)

    def pop(self):
        if len(self.val)==0:
            return -1
        x=self.val[-1]
        self.val.pop()
        return x
    def top(self):
        if len(self.val)==0:
            return -1
        return self.val[-1]

    def top2(self):
        if len(self.val) <2:
            return -1
        return self.val[-2]
    
    
    def size(self):
        return len(self.val)

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st=stack()
        for ch in operations:
            if ch not in "CD+":
                st.push(int(ch))

            else:
                if ch=="+":
                    ans=st.top()+st.top2()
                    st.push(ans)
                if ch=="D":
                    st.push(2*st.top())

                if ch=="C":
                    st.pop()

        return sum(st.val)

        