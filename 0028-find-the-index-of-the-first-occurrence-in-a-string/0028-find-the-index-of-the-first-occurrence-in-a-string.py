class Solution(object):
    def strStr(self, haystack, needle):
        if len(needle)==0:
            return -1
        answer=-1
        for i in range(len(haystack)):
            if haystack[i]==needle[0] and i+len(needle)-1<len(haystack):
                check=True
                for j in range(len(needle)):
                    if needle[j]!=haystack[i+j]:
                        check=False
                        break
                if check:
                    answer=i
                    break
        return answer


        