class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashval={}
        largest=nums[0] 
        for i in nums:
            if i in hashval:
                hashval[i]+=1
            else:
                hashval[i]=1
               
            if hashval[i]>hashval[largest]:
                largest=i
        return largest