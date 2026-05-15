class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        order=[]
        for i in range(n):
            order.append(i+1)
        current=0
        while len(order)>1:
             current+=(k-1)
             current=current%len(order)
             order.pop(current)
        return order[0]
        