class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 1000000000
        max_profit = 0

        for i in range(len(prices)):
            profit = prices[i]-min_price

            if min_price > prices[i]:
                min_price = prices[i]
            max_profit = max(max_profit, profit)


        return max_profit 