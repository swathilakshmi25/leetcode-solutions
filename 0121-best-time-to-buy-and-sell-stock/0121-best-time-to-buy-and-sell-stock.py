class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for current_price in prices[1:]:
            profit = max(profit, current_price-buy_price)

            if current_price < buy_price:
                buy_price = current_price

        return profit