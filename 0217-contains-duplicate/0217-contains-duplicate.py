class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashval={}
        for i in nums:
            if i in hashval:
                return True
            hashval[i]=1
        return False