class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 123456789
        max_profit = 0

        for i in range(len(prices)):
            profit = prices[i]-min_price
            min_price = min(min_price,prices[i])
            max_profit = max(max_profit,profit)

        return max_profit