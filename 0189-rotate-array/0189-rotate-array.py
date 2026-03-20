class Solution(object):
    def rotate(self, nums, k):
        a=deque(nums)
        for i in range(k):
            a.appendleft(a.pop())
        for i in range(len(nums)):
            nums[i]=a.popleft()

    
    