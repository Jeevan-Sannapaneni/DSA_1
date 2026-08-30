
"""
Problem 102: Best Time to Buy and Sell Stock II

Difficulty: Medium

Problem Statement:
Given an array of stock prices, find the maximum profit
you can achieve.

You may make as many transactions as you want, but you
must sell the stock before buying again.

Input:
N
N space-separated integers representing stock prices.

Output:
Maximum possible profit.

Time Complexity: O(N)
Space Complexity: O(1)
"""

n = int(input())
prices = list(map(int, input().split()))

profit = 0

for i in range(1, n):

    # If today's price is higher than yesterday's,
    # take that profit.
    if prices[i] > prices[i - 1]:
        profit += prices[i] - prices[i - 1]

print(profit)
