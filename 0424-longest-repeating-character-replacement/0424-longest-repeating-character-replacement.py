class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxfreq={}
        maxi=0
        l=0
        answer=0
        for r in range(len(s)):
            maxfreq[s[r]]=1+maxfreq.get(s[r],0)
            maxi=max(maxi,maxfreq[s[r]])
            while (r-l)+1-maxi>k:
                maxfreq[s[l]]-=1
                l+=1
            answer=max(answer,(r-l+1))
        return answer



        