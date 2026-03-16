class Solution(object):
    def maxTurbulenceSize(self, arr):
        shift=""
        window={}
        l=0
        answer=0
        equal=True
        for i in range(1,len(arr)):
            if arr[i]!=arr[i-1]:
                equal=False
                break
        if equal:
            return 1
        for r in range(1,len(arr)):
            window[arr[r-1]]=1+window.get(arr[r-1],0)
            
            if arr[r]>arr[r-1]:
                if shift=="r":
                    while r-1>l:
                        arr[l]-=1
                        l+=1

                else:
                    shift="r"
                    
                    answer=max(answer,r-l+1)

            elif arr[r]<arr[r-1]:
                if shift=="l":
                    while r-1>l:
                        arr[l]-=1
                        l+=1

                else:
                    shift="l"
                   
                    answer=max(answer,r-l+1)
            else:
                
                while r>l:
                        arr[l]-=1
                        l+=1
        return answer


        