class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        ans, curBottles = numBottles, 0
        while True:
            if numBottles - numExchange < 0:
                numBottles += curBottles
                ans += curBottles
                curBottles = 0
            curBottles += 1
            numBottles -= numExchange
            if numBottles < 0: break
        return ans