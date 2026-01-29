class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashval=set()
        for i in nums:
            if i in hashval:
                return True
            hashval.add(i)
        return False