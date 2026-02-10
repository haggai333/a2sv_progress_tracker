class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer=[]
        ansdic={}
        for i in nums:
            if i in ansdic:
                ansdic[i]+=1
            else:
                ansdic[i]=1
            if i not in answer and ansdic[i]>1:
                answer.append(i)

        return answer

        