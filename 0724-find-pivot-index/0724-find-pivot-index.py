class Solution(object):
    def pivotIndex(self, nums):
        rightsum=[]
        leftsum=[]
        sumi=0
        for i in nums:
            sumi+=i
            leftsum.append(sumi)
        for i in nums:
            rightsum.append(sumi)
            sumi-=i
        answer=-1
        for i in range(len(nums)):
            if rightsum[i]==leftsum[i]:
                answer=i
                break
        return answer

        