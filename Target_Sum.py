# File: 116_Target_Sum.py

"""
Problem: Target Sum
Difficulty: Medium

Problem Statement:
Given an array of integers, assign either '+' or '-' to every
element so that the resulting expression equals a target value.

Find the total number of different ways to achieve the target.

Input:
First line: N (number of elements)
Second line: N space-separated integers
Third line: Target value

Output:
Print the number of ways to achieve the target.

Time Complexity: O(N * S)
Space Complexity: O(S)

Where:
S = sum of all elements
"""

n = int(input())
nums = list(map(int, input().split()))
target = int(input())

# dp[sum] = number of ways to obtain this sum
dp = {0: 1}

for num in nums:
    new_dp = {}

    for current_sum, ways in dp.items():
        # Add '+'
        new_dp[current_sum + num] = (
            new_dp.get(current_sum + num, 0) + ways
        )

        # Add '-'
        new_dp[current_sum - num] = (
            new_dp.get(current_sum - num, 0) + ways
        )

    dp = new_dp

print(dp.get(target, 0))
