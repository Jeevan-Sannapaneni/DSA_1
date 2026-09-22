"""
Problem: Permutation in String
Difficulty: Medium

Problem Statement:
Given two strings s1 and s2, determine whether s2 contains a
substring that is a permutation of s1.

A permutation contains exactly the same characters with the same
frequencies, but the order can be different.

Input:
First line: String s1
Second line: String s2

Output:
Print YES if a permutation of s1 exists in s2.
Otherwise, print NO.

Time Complexity: O(N)
Space Complexity: O(1)
"""

from collections import Counter

s1 = input().strip()
s2 = input().strip()

if len(s1) > len(s2):
    print("NO")
else:
    required = Counter(s1)
    window = Counter()

    left = 0
    window_size = len(s1)

    for right in range(len(s2)):
        window[s2[right]] += 1

        # Keep the window size equal to s1
        if right - left + 1 > window_size:
            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            left += 1

        if window == required:
            print("YES")
            break
    else:
        print("NO")
