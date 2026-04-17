class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxProfit = 0

        while sell < len(prices):
            # is it profitable?
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit,profit)
                sell += 1 # check for more
            else:
                # we found a new low
                buy = sell
                sell = buy + 1

        return maxProfit
