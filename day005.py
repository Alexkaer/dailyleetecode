"""
地址：https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

描述：
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

思路：
由于我们是想获取到最大的利润，我们的策略应该是低点买入，高点卖出。

由于题目对于交易次数有限制，只能交易一次，因此问题的本质其实就是求波峰浪谷的差值的最大值。


"""


class Solution:
    @staticmethod
    def maxProfit(prices):
        if len(prices) == 0:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, prices[i] - minPrice)
            # if prices[i] < minPrice:
            #     minPrice = prices[i]
            # if prices[i] - minPrice > maxProfit:
            #     maxProfit = prices[i] - minPrice
        return maxProfit


print(Solution.maxProfit([7, 1, 5, 3, 6, 4]))
