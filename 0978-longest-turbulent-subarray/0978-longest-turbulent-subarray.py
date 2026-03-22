class Solution(object):
    def maxTurbulenceSize(self, arr):
        shift=""
        l=0
        answer=0
        if len(set(arr))==1:
            return 1
        for r in range(1,len(arr)):
            
            if arr[r]>arr[r-1]:
                if shift=="r":
                        l=r-1

                else:
                    shift="r"
                    
                    answer=max(answer,r-l+1)

            elif arr[r]<arr[r-1]:
                if shift=="l":
                    
                        l=r-1

                else:
                    shift="l"
                   
                    answer=max(answer,r-l+1)
            else:
                        l=r
        return answer



        