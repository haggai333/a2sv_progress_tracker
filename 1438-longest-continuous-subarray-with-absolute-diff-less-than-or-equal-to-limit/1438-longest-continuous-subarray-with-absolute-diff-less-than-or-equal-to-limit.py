class Solution(object):
    def longestSubarray(self, nums, limit):
        mini=deque()
        maxi=deque()
        l=0
        answer=0
        for r,val in enumerate(nums):
            while mini and val<nums[mini[-1]]:
                mini.pop()
            mini.append(r)
            while maxi and  val>nums[maxi[-1]]:
                maxi.pop()
            maxi.append(r)
            while len(maxi)>0 and len(mini)>0 and nums[maxi[0]]-nums[mini[0]]>limit:
                if maxi[0]==l:
                    maxi.popleft()
                if mini[0]==l:
                    mini.popleft()
                l+=1
            answer=max(answer,r-l+1)
        return answer

        
        