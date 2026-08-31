
"""
Problem 104: Best Time to Buy and Sell Stock IV

Difficulty: Hard

Problem Statement:
Given an array of stock prices and an integer K,
find the maximum profit you can achieve with at most
K transactions.

A transaction consists of buying one stock and later
selling it.

You cannot hold more than one stock at a time.

Input:
N
N space-separated integers representing stock prices.
K

Output:
Maximum possible profit.

Time Complexity: O(N * K)
Space Complexity: O(K)
"""

n = int(input())
prices = list(map(int, input().split()))
k = int(input())

if n == 0 or k == 0:
    print(0)
else:

    # If K is large enough, this becomes the unlimited
    # transactions problem.
    if k >= n // 2:

        profit = 0

        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        print(profit)

    else:

        # buy[j]  = maximum profit after buying in the
        #            j-th transaction.
        #
        # sell[j] = maximum profit after selling in the
        #            j-th transaction.

        buy = [float("-inf")] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:

            for transaction in range(1, k + 1):

                buy[transaction] = max(
                    buy[transaction],
                    sell[transaction - 1] - price
                )

                sell[transaction] = max(
                    sell[transaction],
                    buy[transaction] + price
                )

        print(sell[k])
