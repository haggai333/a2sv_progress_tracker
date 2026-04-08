class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        next={}
        line=deque()
        for i in nums2:

            while len(line)>0 and line[-1]<i:
                next[line[-1]]=i
                line.pop()
            line.append(i)
        while len(line)>0:
            next[line[-1]]=-1
            line.pop()

        answer=[]
        for i in nums1:
            answer.append(next.get(i,-1))

        return answer

        