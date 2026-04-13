class Solution(object):
    def evalRPN(self, tokens):
        a=[]
        for i in tokens:
            if i in {"+", "-", "*", "/"}:
                b=a.pop()
                c=a.pop()
                if i=="+":
                    a.append(c+b)
                elif i=="-":
                    a.append(c-b)
                elif i=="*":
                    a.append(c*b)
                else:
                    sign=1
                    if (c*b)<0:
                        sign=-1
                    a.append(sign*(abs(c)//abs(b)))
            else:
                a.append(int(i))
           
        return a.pop()