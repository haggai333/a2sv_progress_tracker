class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer=0
        counts=set()
        r=0
        l=0
        while r<len(s):
            print(counts)
            if s[r] in counts:
                counts.discard(s[l])
                counts.add(s[r])
                r+=1
                l+=1
                
            else:
                counts.add(s[r])
                r+=1
                answer=max(answer,len(counts))
        return answer

        