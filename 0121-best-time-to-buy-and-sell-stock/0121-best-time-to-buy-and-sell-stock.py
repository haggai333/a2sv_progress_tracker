class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=0
        print(mini)
        answer=0
        for i in range(1,len(prices)):
            answer=max(answer,prices[i]-prices[mini])
            if prices[mini]>prices[i]:
                mini=i
        return answer
        
        