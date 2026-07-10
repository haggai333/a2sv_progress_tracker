class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if flowerbed and flowerbed[0]==0:
            if len(flowerbed)>1:
                if flowerbed[1]==0 and n>0:
                    n-=1
                    flowerbed[0]=1
            else:
                n-=1
                flowerbed[0]=1
        
        if flowerbed and flowerbed[-1]==0:
            if len(flowerbed)>1:
                if flowerbed[-2]==0 and n>0:
                    n-=1
                    flowerbed[-1]=1
            else:
                n-=1
                flowerbed[-1]=1
        for i in range(1,len(flowerbed)-1):
            if n==0:
                break
            if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
        return n<=0
        
        