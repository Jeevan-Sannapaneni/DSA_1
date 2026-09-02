

"""
Problem 108: Longest Palindromic Subsequence

Difficulty: Medium

Problem Statement:
Given a string, find the length of its longest subsequence
that is also a palindrome.

A subsequence does not need to be contiguous.

Input:
A string

Output:
Length of the longest palindromic subsequence.

Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""

s = input().strip()

n = len(s)

if n == 0:
    print(0)
else:

    dp = [[0] * n for _ in range(n)]

    # Every single character is a palindrome of length 1.
    for i in range(n):
        dp[i][i] = 1

    # Consider substrings of increasing length.
    for length in range(2, n + 1):

        for left in range(n - length + 1):

            right = left + length - 1

            if s[left] == s[right]:

                if length == 2:
                    dp[left][right] = 2
                else:
                    dp[left][right] = (
                        dp[left + 1][right - 1] + 2
                    )

            else:

                dp[left][right] = max(
                    dp[left + 1][right],
                    dp[left][right - 1]
                )

    print(dp[0][n - 1])
