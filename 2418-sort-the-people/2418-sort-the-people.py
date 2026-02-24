class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size=len(names)
        for i in range(size):
            for j in range(size-i-1):
                if heights[j+1]>heights[j]:
                    temp=heights[j]
                    temp2=names[j]
                    names[j]=names[j+1]
                    heights[j]=heights[j+1]
                    heights[j+1]=temp
                    names[j+1]=temp2
            return names
        