class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            l=0
            r=len(i)-1
            while(r>l):
                temp=i[l]
                i[l]=abs(i[r]-1)
                i[r]=abs(temp-1)
                l+=1
                r-=1
            if len(i)%2==1:
                p=len(i)//2
                i[p]=abs(i[p]-1)
        return image


        