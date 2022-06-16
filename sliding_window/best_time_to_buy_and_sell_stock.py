class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # l=buy, r=sell
        max_profit = 0

        while r < len(prices):

            # profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r

            r += 1

        return max_profit