class Solution(object):
    def isValid(self, s):
        stack=[]
        for i in s:
            if i=="(" or i=="{" or i=="[":
                stack.append(i)
            else:
                if len(stack)>=1:
                    c=stack[-1]
                else:
                    return False
                if c=="{" and i=="}" or c=="[" and i=="]" or c=="(" and i==")":
                    stack.pop()
                else:
                    return False
        return len(stack)==0

        