class Solution(object):
    def removeStars(self, s):
        count=0
        stack=[]
        for i in s:
            if i!="*":
                stack.append(i)
            else:
                if len(stack)>0:
                    stack.pop()
            
        return "".join(stack)

        