class Solution(object):
    def nextGreaterElements(self, nums):
        line=deque()
        l=nums+nums
        size=len(nums)
        next={}
        for i,val in enumerate(l):
            while len(line)>0 and nums[line[-1]%size]<val:
                next[line[-1]]=i%size
                line.pop()
            line.append(i)
        answer=[]
        for i in range(len(nums)):
            if i not in next:
                answer.append(-1)
            else:
                answer.append(nums[next[i]])
        return answer
        
        