
"""
Problem: Longest Palindromic Substring
Difficulty: Medium

Problem Statement:
Given a string, find the longest substring that reads the same
forward and backward.

Input:
A single string.

Output:
Print the longest palindromic substring.

Time Complexity: O(N^2)
Space Complexity: O(1)
"""

s = input().strip()


def expand_from_center(left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return s[left + 1:right]


longest = ""

for i in range(len(s)):
    # Odd-length palindrome
    palindrome1 = expand_from_center(i, i)

    # Even-length palindrome
    palindrome2 = expand_from_center(i, i + 1)

    if len(palindrome1) > len(longest):
        longest = palindrome1

    if len(palindrome2) > len(longest):
        longest = palindrome2

print(longest)
