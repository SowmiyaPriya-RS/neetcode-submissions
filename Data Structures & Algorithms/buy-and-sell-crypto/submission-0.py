class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minbuy = prices[0]
        for price in prices:
            profit = max(profit, price-minbuy)
            minbuy = min(minbuy, price)
        return profit
        