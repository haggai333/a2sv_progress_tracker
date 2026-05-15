class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        l = 0
        window = set()
        for r in range(len(s)):
            while s[r] in window:
                window.discard(s[l])
                l += 1
            window.add(s[r])
            answer = max(answer, r - l + 1)
        return answer
