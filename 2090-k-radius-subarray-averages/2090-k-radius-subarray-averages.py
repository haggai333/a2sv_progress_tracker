class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        size= len(nums)
        winsize =2*k+1
        answer=[-1]*size
        if winsize>size:
            return answer
        prefixsum=[0]*(size+1)
        for i in range(size):
            prefixsum[i+1]=prefixsum[i]+nums[i]
        for i in range(k,size-k):
            total=prefixsum[i+k+1]-prefixsum[i-k]
            answer[i]=total//winsize
        return answer 
        