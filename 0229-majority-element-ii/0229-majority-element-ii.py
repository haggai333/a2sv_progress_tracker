class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashval={}
        answer=[]
        for i in nums:
            if i in hashval:
                hashval[i]+=1
            else:
                hashval[i]=1
           
            if hashval[i]>len(nums)//3:
                answer.append(i)
                hashval[i]=0
        return answer