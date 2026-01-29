class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashval={}
        for i in nums:
            if i in hashval:
                hashval[i]+=1
            else:
                hashval[i]=1
        largest=nums[0]        
        for i in hashval:
            if hashval[i]>hashval[largest]:
                largest=i
        return largest