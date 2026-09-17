
"""
Problem: Maximum Subarray
Difficulty: Medium

Problem Statement:
Given an integer array, find the contiguous subarray with the
largest possible sum.

The subarray must contain at least one element.

Input:
First line: N (number of elements)
Second line: N space-separated integers

Output:
Print the maximum subarray sum.

Time Complexity: O(N)
Space Complexity: O(1)
"""

n = int(input())
nums = list(map(int, input().split()))

current_sum = nums[0]
maximum_sum = nums[0]

for i in range(1, n):
    current_sum = max(nums[i], current_sum + nums[i])
    maximum_sum = max(maximum_sum, current_sum)

print(maximum_sum)
