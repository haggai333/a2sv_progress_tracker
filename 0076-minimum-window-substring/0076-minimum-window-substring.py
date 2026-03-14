class Solution(object):
    def minWindow(self, s, t):
        count = {}
        ht = {}
        counter = {}

        for char in t:
            ht[char] = 1 + ht.get(char, 0)

        l = 0
        li = 0
        ri = 0
        size = 999999

        for r in range(len(s)):

            if s[r] in ht:
                counter[s[r]] = counter.get(s[r], 0) + 1

                if counter[s[r]] <= ht[s[r]]:
                    count[s[r]] = counter[s[r]]

            while count == ht:

                if r - l + 1 < size:
                    size = r - l + 1
                    li = l
                    ri = r

                if s[l] in counter:
                    counter[s[l]] -= 1

                    if counter[s[l]] < ht[s[l]]:
                        if s[l] in count:
                            del count[s[l]]

                l += 1

        if size != 999999:
            return s[li:ri+1]
        return ""