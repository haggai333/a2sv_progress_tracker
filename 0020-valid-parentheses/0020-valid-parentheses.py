class Solution(object):
    def isValid(self, s):
        close=set("})]")
        check={"}":"{",")":"(","]":"["}
        stack=list()
        for i in s:
            if i not in close:
                stack.append(i)
            else:
                if not stack or  (stack[-1]!=check[i]):
                    return False
                stack.pop()
        return len(stack)==0
