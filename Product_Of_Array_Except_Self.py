"""
Problem: Product of Array Except Self
Difficulty: Medium

Problem Statement:
Given an array of integers, return an array where each element
is the product of all elements in the original array except itself.

Do not use division.

Input:
First line: N (number of elements)
Second line: N space-separated integers

Output:
Print the resulting array.

Time Complexity: O(N)
Space Complexity: O(1) extra space
"""

n = int(input())
nums = list(map(int, input().split()))

result = [1] * n

# Store products of all elements to the left
prefix = 1

for i in range(n):
    result[i] = prefix
    prefix *= nums[i]

# Multiply by products of all elements to the right
suffix = 1

for i in range(n - 1, -1, -1):
    result[i] *= suffix
    suffix *= nums[i]

print(*result)
