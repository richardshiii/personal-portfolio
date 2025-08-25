'''
122. Best Time to Buy and Sell Stock II
Difficulty: Medium
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
'''
# Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # T: O(n): iterate through the input array
        # S: O(1): no extra space required
        # initialize max_profit to 0
        max_profit = 0
        # start from the second day and iterate through the prices array
        for i in range(1, len(prices)):
            # find days we can make profit
            if prices[i] > prices[i-1]:
                # accumulate the profit as we iterate through the prices array
                max_profit += prices[i] - prices[i-1]
        return max_profit
    
'''
Test Case
prices = [7,1,5,3,6,4]
Output
7
'''