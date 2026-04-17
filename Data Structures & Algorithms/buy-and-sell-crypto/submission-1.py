class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxProfit = 0

        while sell < len(prices):
            buyAmount, sellAmount = prices[buy], prices[sell]
            profit = sellAmount - buyAmount
            #print("Comp ",prices.index(buyAmount),":",buyAmount, " and ",prices.index(sellAmount),':', sellAmount, " with profit ", profit)
            if profit > maxProfit:
                maxProfit = profit
            
            if buyAmount > sellAmount:
                buy += 1
                sell = buy + 1
            else:
                sell += 1

        return maxProfit
