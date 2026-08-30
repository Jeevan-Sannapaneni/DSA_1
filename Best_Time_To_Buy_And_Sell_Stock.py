

"""
Problem 101: Best Time to Buy and Sell Stock

Difficulty: Easy

Problem Statement:
Given an array of stock prices where prices[i] is the
price of a stock on day i, find the maximum profit you
can achieve by buying on one day and selling on a later day.

You can complete at most one transaction.

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

minimum_price = float("inf")
maximum_profit = 0

for price in prices:

    minimum_price = min(minimum_price, price)

    profit = price - minimum_price

    maximum_profit = max(maximum_profit, profit)

print(maximum_profit)
