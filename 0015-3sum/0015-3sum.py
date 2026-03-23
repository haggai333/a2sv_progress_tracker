class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        answer=[]
        for l,val in enumerate(nums):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            li = l + 1
            ri=len(nums)-1
            if nums[l]>0:
                break
            while ri>li:
                if nums[ri]+nums[l]+nums[li]>0:
                    ri-=1
                elif nums[ri]+nums[li]+nums[l]<0:
                    li+=1
                else:
                    answer.append([nums[l],nums[li],nums[ri]])
                    li+=1
                    ri-=1
                    while li < ri and nums[li]==nums[li-1]:
                        li+=1
                    while li<ri and nums[ri]==nums[ri+1]:
                        ri-=1
        return answer



        

                


        
            



                


        
        