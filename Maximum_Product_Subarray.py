"""
Problem: Maximum Product Subarray
Difficulty: Medium

Problem Statement:
Given an integer array, find the contiguous subarray that has
the largest product.

The subarray must contain at least one element.

Input:
First line: N (number of elements)
Second line: N space-separated integers

Output:
Print the maximum product of any contiguous subarray.

Time Complexity: O(N)
Space Complexity: O(1)
"""

n = int(input())
nums = list(map(int, input().split()))

current_max = nums[0]
current_min = nums[0]
answer = nums[0]

for i in range(1, n):
    num = nums[i]

    # A negative number can turn the minimum into the maximum
    if num < 0:
        current_max, current_min = current_min, current_max

    current_max = max(num, current_max * num)
    current_min = min(num, current_min * num)

    answer = max(answer, current_max)

print(answer)
