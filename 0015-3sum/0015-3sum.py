class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        i=0
        j=0
        k=0
        answer=[]
        nums.sort()
        while i<len(nums)-2:
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            j=i+1
            k=len(nums)-1
            while k>j:
                if nums[k]+nums[j]+nums[i]>0:
                    k-=1
                elif nums[k]+nums[j]+nums[i]<0:
                    j+=1
                else:
                    answer.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while k>j and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
            i+=1
        return answer


        