# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you
# must buy before you sell.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        max_profit = 0
        min_purchase = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_purchase)
            min_purchase = min(min_purchase, prices[i])
        return max_profit


# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         left = 0
#         right = 1
#
#         max_profit = 0
#
#         while right < len(prices):
#             current_profit = prices[right] - prices[left]
#
#             if prices[left] < prices[right]:
#                 max_profit = max(current_profit, max_profit)
#             else:
#                 left = right
#
#             right += 1
#
#
#         return max_profit



# def maxProfit(self, prices: list[int]) -> int:
#     return max(j - k for j, k in zip(prices, accumulate(prices, min)))

sol = Solution()
stocks = [2, 4, 1]
res = sol.maxProfit(stocks)
print(res)