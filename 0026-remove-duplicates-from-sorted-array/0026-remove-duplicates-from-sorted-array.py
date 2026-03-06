class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        answer=[]
        answer.append(nums[0])
        current=0
        for i in range(0,len(nums)):
            if answer[current]==nums[i]:
                continue
            answer.append(nums[i])
            current+=1
        nums.clear()
        for i in answer:
            nums.append(i)
        


        