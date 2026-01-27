class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        result=0
        while numBottles>=numExchange:
            result+=numExchange
            numBottles-=numExchange
            numBottles+=1
            
            

        return result +numBottles

        