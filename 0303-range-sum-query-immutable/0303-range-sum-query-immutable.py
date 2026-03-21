class NumArray(object):

    def __init__(self, nums):
        self.prefix=[]
        sumi=0
        for i in nums:
            sumi+=i
            self.prefix.append(sumi)

    def sumRange(self, left, right):
        rightsum=self.prefix[right]
        leftsum=self.prefix[left-1] if left>0 else 0
        return rightsum -leftsum
        
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)