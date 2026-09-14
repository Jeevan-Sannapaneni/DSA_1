
"""
Problem: Longest Substring Without Repeating Characters
Difficulty: Medium

Problem Statement:
Given a string, find the length of the longest substring that
contains no repeated characters.

Input:
A single string.

Output:
Print the length of the longest substring without duplicate characters.

Time Complexity: O(N)
Space Complexity: O(N)
"""

s = input().strip()

last_seen = {}
left = 0
maximum = 0

for right in range(len(s)):
    char = s[right]

    # Move left past the previous occurrence
    if char in last_seen and last_seen[char] >= left:
        left = last_seen[char] + 1

    last_seen[char] = right

    maximum = max(maximum, right - left + 1)

print(maximum)
