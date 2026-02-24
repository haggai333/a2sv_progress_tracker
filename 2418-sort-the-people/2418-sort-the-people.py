class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            for j in range(i,len(names)-1):
                if heights[j+1]>heights[j]:
                    temp=heights[j]
                    temp2=names[j]
                    names[j]=names[j+1]
                    heights[j]=heights[j+1]
                    heights[j+1]=temp
                    names[j+1]=temp2
        return names
        