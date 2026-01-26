class Solution(object):
    def longestCommonPrefix(self, strs):
        a=strs[0]
        for b in strs:
            answ=''
            mi=min(len(a),len(b))
            for k in range(mi):
                if a[k]==b[k]:
                    answ+=a[k]
                    continue
                break
            
            a=answ
        return a

        