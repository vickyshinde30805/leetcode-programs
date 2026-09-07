class stack:
    def __init__ (self):
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

    def size(self):
        return len(self.val)




class Solution:
    def isValid(self, s: str) -> bool:
        st=stack()
        for ch in s:
            if ch in "({[":
                st.push(ch)

            else:
                if st.size()==0:
                    return False
                
                top=st.pop()

                if (
                   (ch==")"and top!="(") or 
                   (ch=="}"and top!="{") or
                   ( ch=="]" and top !="[")
                   ):
                    return False
                
                

        return st.size()==0
            

      

        

        