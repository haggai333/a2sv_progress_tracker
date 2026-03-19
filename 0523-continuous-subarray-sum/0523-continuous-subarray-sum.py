class Solution(object):
    def checkSubarraySum(self, nums, k):
        
        sumi=[]
        su=0
        for i in nums:
            su+=i
            sumi.append(su)
        oki=[]
        for i in range(len(sumi)):
            oki.append(sumi[i]%k)

        for i in range(1,len(oki)):
            if oki[i]%k==0:
                return True
        counter={}
        for i in range(len(nums)):
            if oki[i] in counter:
                if i-counter[oki[i]]>1:
                    return  True
            else:
                counter[oki[i]]=i

        return False
            


        
        


        