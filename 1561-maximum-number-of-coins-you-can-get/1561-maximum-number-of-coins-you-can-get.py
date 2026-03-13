class Solution(object):
    def maxCoins(self, piles):
        piles.sort(reverse=True)
        result=0
        canpick=((len(piles)/3)*2)+1
        for i in range(1,canpick,2):
            result+=piles[i]
        return result
        