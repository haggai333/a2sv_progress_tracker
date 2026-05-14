class Solution(object):
    def isGood(self, nums):
        seen={}
        special=len(nums)-1
        for i in nums:
            seen[i]=1+seen.get(i,0)
        if special not in seen or seen[special]!=2:
            return False
        for i in range(1,len(nums)):
            if i not in seen or (seen[i]>1 and i!=special):
                return False
        return True

        
        return count==2
        