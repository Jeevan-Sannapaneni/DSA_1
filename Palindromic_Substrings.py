
"""
Problem: Palindromic Substrings
Difficulty: Medium

Problem Statement:
Given a string, count the total number of substrings that are
palindromes.

Every occurrence is counted separately.

Input:
A single string.

Output:
Print the total number of palindromic substrings.

Time Complexity: O(N^2)
Space Complexity: O(1)
"""

s = input().strip()

count = 0


def count_from_center(left, right):
    total = 0

    while left >= 0 and right < len(s) and s[left] == s[right]:
        total += 1
        left -= 1
        right += 1

    return total


for i in range(len(s)):
    # Odd-length palindromes
    count += count_from_center(i, i)

    # Even-length palindromes
    count += count_from_center(i, i + 1)

print(count)
