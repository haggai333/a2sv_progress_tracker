class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashval={}
        for i in nums:
            if i in hashval:
                hashval[i]+=1
            else:
                hashval[i]=1
               
        
        return max(hashval,key=hashval.get)