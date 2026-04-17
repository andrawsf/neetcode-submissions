class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxProfit = 0

        while sell < len(prices):
            buyAmount, sellAmount = prices[buy], prices[sell]
            profit = sellAmount - buyAmount
            
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit,profit)
                sell += 1
            else:
                buy = sell
                sell = buy + 1

        return maxProfit
