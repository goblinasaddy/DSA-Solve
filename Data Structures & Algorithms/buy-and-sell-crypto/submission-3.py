class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=100000000
        maxi=0

        for i in range(len(prices)):
            profit=prices[i]-min_price

            if prices[i]<min_price:
                min_price=prices[i]

            if maxi<profit:
                maxi=profit

        return maxi