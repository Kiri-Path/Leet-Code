class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def max_profit(prices):
            if not prices:
                return 0
            
            max_profit = 0 
            min_price = prices[0]

            for price in prices:
                if price < min_price:
                    min_price = price
                else:
                    max_profit += price - min_price
                    min_price = price
                
            return max_profit
