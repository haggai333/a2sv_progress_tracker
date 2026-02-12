class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        mapans={}
        size=len(s)
        for i in range(size):
            mapans[indices[i]]=s[i]
        answer=""
        for i in range(size):
            answer+=str(mapans[i])
        return answer