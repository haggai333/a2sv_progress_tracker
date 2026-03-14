class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer=0
        counts=set()
        r=0
        l=0
        while r<len(s):
            if s[r] in counts:
                while l<=r:
                    if s[l]==s[r]:
                        counts.discard(s[l])
                        l+=1
                        break
                    counts.discard(s[l])
                    l+=1
            counts.add(s[r])
            r+=1
            answer=max(answer,len(counts))
        return answer

        