
"""
Problem 105: Longest Common Subsequence

Difficulty: Medium

Problem Statement:
Given two strings, find the length of their Longest Common
Subsequence (LCS).

A subsequence is a sequence that appears in the same
relative order but not necessarily contiguously.

Input:
String 1
String 2

Output:
Length of the Longest Common Subsequence.

Time Complexity: O(N × M)
Space Complexity: O(N × M)
"""

text1 = input().strip()
text2 = input().strip()

n = len(text1)
m = len(text2)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):

    for j in range(1, m + 1):

        if text1[i - 1] == text2[j - 1]:

            dp[i][j] = dp[i - 1][j - 1] + 1

        else:

            dp[i][j] = max(
                dp[i - 1][j],
                dp[i][j - 1]
            )

print(dp[n][m])
