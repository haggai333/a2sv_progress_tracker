class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        answer=0
        for i in prices:
            answer=max(answer,i-mini)
            if mini>i:
                mini=i
        return answer
        
        