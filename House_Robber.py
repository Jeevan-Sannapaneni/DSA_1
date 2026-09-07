"""
Problem: House Robber
Difficulty: Medium

Problem Statement:
You are planning to rob houses along a street.

Each house contains a certain amount of money.
You cannot rob two adjacent houses because the alarm will be triggered.

Find the maximum amount of money you can rob.

Input:
First line: N (number of houses)
Second line: N space-separated amounts of money

Output:
Print the maximum amount of money that can be robbed.

Time Complexity: O(N)
Space Complexity: O(1)
"""

n = int(input())
money = list(map(int, input().split()))

if n == 0:
    print(0)
elif n == 1:
    print(money[0])
else:
    prev2 = 0
    prev1 = 0

    for amount in money:
        current = max(prev1, prev2 + amount)
        prev2 = prev1
        prev1 = current

    print(prev1)
