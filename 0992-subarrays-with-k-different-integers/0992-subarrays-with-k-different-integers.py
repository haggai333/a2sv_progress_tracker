class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        l=0
        count={}
        answer=0
        temp=k
        answer1=0
        for r,val in enumerate(nums):
            count[val]=1+count.get(val,0)
            if count[val]==1:
                k-=1
            while k<0:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    k+=1
                l += 1
            answer+=r-l+1
        k=temp-1
        count.clear()
        l=0
        for r,val in enumerate(nums):
            count[val]=1+count.get(val,0)
            if count[val]==1:
                k-=1
            while k<0:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    k+=1
                l += 1
            answer1+=r-l+1
            
        return answer-answer1
        