
"""
Problem: Container With Most Water
Difficulty: Medium

Problem Statement:
Given an array of heights where each value represents the height
of a vertical line, find two lines that together with the x-axis
form a container that holds the maximum amount of water.

Input:
First line: N (number of lines)
Second line: N space-separated heights

Output:
Print the maximum amount of water the container can hold.

Time Complexity: O(N)
Space Complexity: O(1)
"""

n = int(input())
heights = list(map(int, input().split()))

left = 0
right = n - 1
maximum_area = 0

while left < right:
    width = right - left
    height = min(heights[left], heights[right])

    area = width * height
    maximum_area = max(maximum_area, area)

    # Move the pointer with the smaller height
    if heights[left] < heights[right]:
        left += 1
    else:
        right -= 1

print(maximum_area)
