# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        answer1=[]
        answer2=[]
        def search(heads):
            if heads==None:
                answer1.append(heads)
                return 
            answer1.append(heads.val)
            search(heads.left)
            search(heads.right)
        def searchs(heads):
            if heads==None:
                answer2.append(heads)
                return 
            answer2.append(heads.val)
            searchs(heads.left)
            searchs(heads.right)
        search(p)
        searchs(q)
        return answer1==answer2
        