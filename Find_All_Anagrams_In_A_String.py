"""
Problem: Find All Anagrams in a String
Difficulty: Medium

Problem Statement:
Given two strings s and p, find all starting indices in s where
an anagram of p occurs.

Return the indices in increasing order.

Input:
First line: String s
Second line: String p

Output:
Print all starting indices separated by spaces.
If no anagram exists, print -1.

Time Complexity: O(N)
Space Complexity: O(1)
"""

from collections import Counter

s = input().strip()
p = input().strip()

if len(p) > len(s):
    print(-1)
else:
    required = Counter(p)
    window = Counter()

    left = 0
    result = []
    window_size = len(p)

    for right in range(len(s)):
        window[s[right]] += 1

        # Keep the window size equal to p
        if right - left + 1 > window_size:
            window[s[left]] -= 1

            if window[s[left]] == 0:
                del window[s[left]]

            left += 1

        if right - left + 1 == window_size and window == required:
            result.append(left)

    if result:
        print(*result)
    else:
        print(-1)
