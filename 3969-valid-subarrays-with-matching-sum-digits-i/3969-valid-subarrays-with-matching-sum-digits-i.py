class Solution(object):
    def countValidSubarrays(self, nums, x):
        answer=0
        prefix=nums[:]
        x=str(x)
        for i in range(1,len(nums)):
            prefix[i]+=prefix[i-1]
        prefix=[0]+prefix
        for i in range(len(prefix)):
            for j in range(i+1,len(prefix)):
                a=str(prefix[j]-prefix[i])
                if a[0]==x and a[-1]==x:
                    answer+=1
        return answer
                
       
        
        