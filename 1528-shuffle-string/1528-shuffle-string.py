class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        mapans={}
        
        for i in range(len(s)):
            mapans[indices[i]]=s[i]
        answer=""
        for i in range(len(s)):
            answer+=str(mapans[i])
        return answer


        