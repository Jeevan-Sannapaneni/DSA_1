

"""
Problem: Largest Rectangle in Histogram
Difficulty: Hard

Problem Statement:
Given an array of non-negative integers representing the heights
of bars in a histogram, find the area of the largest rectangle
that can be formed using consecutive bars.

Input:
First line: N (number of bars)
Second line: N space-separated heights

Output:
Print the maximum rectangle area.

Time Complexity: O(N)
Space Complexity: O(N)
"""

n = int(input())
heights = list(map(int, input().split()))

stack = []
maximum_area = 0

# Add a zero-height bar to process remaining bars
heights.append(0)

for i, height in enumerate(heights):

    while stack and heights[stack[-1]] > height:
        index = stack.pop()

        bar_height = heights[index]

        if stack:
            width = i - stack[-1] - 1
        else:
            width = i

        area = bar_height * width
        maximum_area = max(maximum_area, area)

    stack.append(i)

print(maximum_area)
