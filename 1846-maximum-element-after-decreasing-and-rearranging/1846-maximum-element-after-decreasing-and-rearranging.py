class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        print(arr)
        arr[0]=1
        maxi=-10000000
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1])>1:
                arr[i]=arr[i-1]+1
            maxi=max(maxi,arr[i])
        return maxi
        