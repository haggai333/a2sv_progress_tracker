class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        for i in arr2:
            if i not in arr1:
                arr1.append(i)
        counter={}
        for i in arr1:
            if i in counter:
                counter[i]+=1
            else:
                counter[i]=1
        
        arr1.sort(key=lambda x: (arr2.index(x) if x in arr2 else 100000 + x))
        return arr1

        
            

            