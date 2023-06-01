# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        min_price = prices[0]  # Initialize min_price to the first element
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit
