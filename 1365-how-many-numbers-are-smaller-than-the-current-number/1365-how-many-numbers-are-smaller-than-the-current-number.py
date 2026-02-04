class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer=[]
        position={}
        j=sorted(nums)
        for i in nums:
            answer.append(j.index(i))
        return answer
            