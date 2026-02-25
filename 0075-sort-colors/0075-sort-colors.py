class Solution:
    def sortColors(self, nums: List[int]) -> None:
        listA=[0,0,0]
        for i in nums:
            listA[i]+=1
        index=0
        for j in range(0,3):
            for i in range(listA[j]):
                nums[index]=j
                index+=1


        