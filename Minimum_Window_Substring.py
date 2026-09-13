
"""
Problem: Minimum Window Substring
Difficulty: Hard

Problem Statement:
Given two strings s and t, find the smallest substring of s that
contains all characters of t, including duplicate characters.

If no such substring exists, print an empty string.

Input:
First line: String s
Second line: String t

Output:
Print the minimum window substring.

Time Complexity: O(N)
Space Complexity: O(M)

Where:
N = length of s
M = number of distinct characters in t
"""

s = input().strip()
t = input().strip()

if not s or not t:
    print("")
else:
    required = {}

    for char in t:
        required[char] = required.get(char, 0) + 1

    window = {}
    formed = 0
    required_count = len(required)

    left = 0
    best_length = float("inf")
    best_start = 0

    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1

        if char in required and window[char] == required[char]:
            formed += 1

        # Try to shrink the window
        while formed == required_count:
            current_length = right - left + 1

            if current_length < best_length:
                best_length = current_length
                best_start = left

            left_char = s[left]
            window[left_char] -= 1

            if (
                left_char in required
                and window[left_char] < required[left_char]
            ):
                formed -= 1

            left += 1

    if best_length == float("inf"):
        print("")
    else:
        print(s[best_start:best_start + best_length])
