class Solution(object):
    def maxCoins(self, piles):
        piles.sort(reverse=True)
        result=0
        canpick=len(piles)/3
        count=0
        for i in range(1,len(piles),2):
            result+=piles[i]
            count+=1
            if canpick==count:
                break

        
        
            
        return result

        