class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        answer=0
        while(r>l):
            if nums[r]+nums[l]==k:
                answer+=1
                r-=1
                l+=1
                continue
            if nums[r]+nums[l]>k:
                r-=1
            else:
                l+=1
        return answer
        