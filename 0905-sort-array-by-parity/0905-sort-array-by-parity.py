class Solution(object):
    def sortArrayByParity(self, nums):
        nums.sort(key =lambda x:(x%2==1,x%2==0))
        return nums
        
        