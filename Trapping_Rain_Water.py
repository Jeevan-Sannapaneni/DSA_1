
"""
Problem: Trapping Rain Water
Difficulty: Hard

Problem Statement:
Given an array of non-negative integers representing an elevation
map, calculate how much rainwater can be trapped after raining.

Input:
First line: N (number of bars)
Second line: N space-separated heights

Output:
Print the total amount of trapped rainwater.

Time Complexity: O(N)
Space Complexity: O(1)
"""

n = int(input())
heights = list(map(int, input().split()))

left = 0
right = n - 1

left_max = 0
right_max = 0

water = 0

while left < right:

    if heights[left] <= heights[right]:

        if heights[left] >= left_max:
            left_max = heights[left]
        else:
            water += left_max - heights[left]

        left += 1

    else:

        if heights[right] >= right_max:
            right_max = heights[right]
        else:
            water += right_max - heights[right]

        right -= 1

print(water)
