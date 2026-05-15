class Solution(object):
    def evalRPN(self, tokens):
        stack=list()
        check=set("/*-+")
        for i in tokens:
            if i not in check:
                stack.append(int((i)))
            else:
                b=stack.pop()
                a=stack.pop()
                if i=="+":
                    stack.append(a+b)
                elif i=="-":
                    stack.append(a-b)
                elif i=="*":
                    stack.append(a*b)
                else:
                    stack.append(int(float(a)/b))
                
        return stack.pop()
        