class Solution(object):
    def isValid(self, s):
        stack=[]
        pairs={"}":"{","]":"[",")":"(","{" :"}","[" :"]" ,"(" :")"}
        for i in s:
            if i=="(" or i=="{" or i=="[":
                stack.append(i)
            else:
                if len(stack)>=1:
                    c=stack[-1]
                else:
                    return False
                if pairs[c]==i:
                    stack.pop()
                else:
                    return False
        return len(stack)==0
        

        