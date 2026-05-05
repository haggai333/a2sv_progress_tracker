class Solution(object):
    def longestCommonPrefix(self, strs):
        a=strs[0].strip()
        for b in strs:
            answ=[]
            mi=min(len(a),len(b))
            for k in range(mi):
                if a[k]==b[k]:
                    answ.append(a[k])
                else:    
                    break
            
            a=answ
        return "".join(a)

        