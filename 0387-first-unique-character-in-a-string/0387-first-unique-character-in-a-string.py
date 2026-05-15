class Solution(object):
    def firstUniqChar(self, s):
        h=Counter(s)
        for i in range(len(s)):
            if h[s[i]]==1:
                return i
        return -1