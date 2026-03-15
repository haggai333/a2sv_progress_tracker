class Solution(object):
    def countGood(self, nums, k):
       counts = Counter()
       l = 0
       simgroup = 0
       answer = 0
       size=len(nums)
       
       for r in range(size):
           simgroup += counts[nums[r]]
           counts[nums[r]] += 1
           
           while simgroup >= k:
               answer += size - r
               counts[nums[l]] -= 1
               simgroup -= counts[nums[l]]
               l += 1
               
       return answer
        
        