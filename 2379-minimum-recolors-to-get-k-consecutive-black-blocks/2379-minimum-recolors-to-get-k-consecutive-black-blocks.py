class Solution(object):
    def minimumRecolors(self, blocks, k):
        window={}
        l=0
        answer=999999
        for r,val in enumerate(blocks):
            if val in window:
                window[val]+=1
            else:
                window[val]=1
            if r-l==k-1:
                if 'W' in window:
                    answer=min(answer,window['W'])
                else:
                    answer=0
                window[blocks[l]]-=1
                l+=1
        return answer