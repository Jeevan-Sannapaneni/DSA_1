
"""
Problem 106: Longest Increasing Subsequence

Difficulty: Medium

Problem Statement:
Given an array of integers, find the length of the
Longest Increasing Subsequence (LIS).

A subsequence does not need to be contiguous.

Input:
N
N space-separated integers

Output:
Length of the LIS.

Time Complexity: O(N log N)
Space Complexity: O(N)
"""

from bisect import bisect_left


n = int(input())
nums = list(map(int, input().split()))

lis = []

for number in nums:

    position = bisect_left(lis, number)

    if position == len(lis):
        lis.append(number)
    else:
        lis[position] = number

print(len(lis))
