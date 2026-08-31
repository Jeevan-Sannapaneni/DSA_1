

"""
Problem 103: Best Time to Buy and Sell Stock III

Difficulty: Hard

Problem Statement:
Given an array of stock prices, find the maximum profit
you can achieve with at most two transactions.

You cannot hold more than one stock at a time.

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

first_buy = float("-inf")
first_sell = 0

second_buy = float("-inf")
second_sell = 0

for price in prices:

    # Best profit after buying the first stock.
    first_buy = max(first_buy, -price)

    # Best profit after selling the first stock.
    first_sell = max(first_sell, first_buy + price)

    # Best profit after buying the second stock.
    second_buy = max(second_buy, first_sell - price)

    # Best profit after selling the second stock.
    second_sell = max(second_sell, second_buy + price)

print(second_sell)
