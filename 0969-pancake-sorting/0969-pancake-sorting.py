class Solution(object):
    def pancakeSort(self, arr):
        answer=[]
        n=len(arr)
        for i in range(n,1,-1):
            maxi=arr.index(i)
            if maxi!=i-1:
                if maxi!=0:
                    answer.append(maxi+1)
                    arr[:maxi+1]=arr[:maxi+1][::-1]
                answer.append(i)
                arr[:i]=arr[:i][::-1]
        return answer



        