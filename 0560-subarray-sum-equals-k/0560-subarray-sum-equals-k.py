class Solution(object):
    def subarraySum(self, nums, k):
        prefix=[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[-1]+nums[i])
        answer=0
        count={}
        for i in prefix:
            if i==k:
                answer+=1
            if i-k in count:
                answer+=count[i-k]
            count[i]=1+count.get(i,0)
        return answer

        print(prefix)

        
        