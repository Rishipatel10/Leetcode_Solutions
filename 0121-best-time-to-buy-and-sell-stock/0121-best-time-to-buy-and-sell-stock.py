class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        profit = 0

        for price in prices:
            min_price = min(min_price,price)
            profit = max(profit,price - min_price)

        return profit

        # max_profit = 0
        # min_price = prices[0]

        # for i in prices:
        #     if i < min_price:
        #         min_price=i
            
        #     profit = i - min_price

        #     if profit > max_profit:
        #         max_profit=profit

        # return max_profit