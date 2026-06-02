# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        self.answer=[]
        def traverse(roots):
            if not roots:
                self.answer.append(None)
                return
            self.answer.append(roots.val)
            traverse(roots.left)
            traverse(roots.right)
        traverse(root)
        first=self.answer
        self.answer=[]
        traverse(subRoot)
        if len(first)<len(self.answer):
            return False
        answer=False
        for i in range(len(first)):
            if answer:
                break
            if first[i]==self.answer[0] and i+len(self.answer)-1<len(first):
                check=True
                for j in range(len(self.answer)):
                    if self.answer[j]!=first[i+j]:
                        check=False
                        break
                if check:
                    answer=True
                    break
        return answer           
        
        
        