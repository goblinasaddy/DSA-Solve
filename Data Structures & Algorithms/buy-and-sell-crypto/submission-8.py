class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')

        maxProfit = 0

        for i in range(len(prices)):
            if prices[i]<min_price: min_price = prices[i]

            profit = prices[i]-min_price

            maxProfit = max(maxProfit,profit)

        return maxProfit if maxProfit != float('inf') else 0