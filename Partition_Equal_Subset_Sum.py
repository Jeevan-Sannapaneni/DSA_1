# File: 115_Partition_Equal_Subset_Sum.py

"""
Problem: Partition Equal Subset Sum
Difficulty: Medium

Problem Statement:
Given an array of positive integers, determine whether it can be
divided into two subsets such that both subsets have the same sum.

Input:
First line: N (number of elements)
Second line: N space-separated integers

Output:
Print YES if the array can be divided into two equal-sum subsets.
Otherwise, print NO.

Time Complexity: O(N * S)
Space Complexity: O(S)

Where:
S = total sum of all elements
"""

n = int(input())
nums = list(map(int, input().split()))

total = sum(nums)

# An odd total sum cannot be divided equally
if total % 2 != 0:
    print("NO")
else:
    target = total // 2

    # dp[i] tells whether a subset with sum i is possible
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for current in range(target, num - 1, -1):
            dp[current] = dp[current] or dp[current - num]

    print("YES" if dp[target] else "NO")
