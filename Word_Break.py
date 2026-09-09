

"""
Problem: Word Break
Difficulty: Medium

Problem Statement:
Given a string and a dictionary of words, determine whether the
string can be completely split into one or more dictionary words.

Each dictionary word can be used multiple times.

Input:
First line: A string s
Second line: N (number of dictionary words)
Third line: N space-separated dictionary words

Output:
Print YES if the string can be segmented into dictionary words.
Otherwise, print NO.

Time Complexity: O(N * L * W)
Space Complexity: O(L)

Where:
L = length of the string
W = maximum word length
"""

s = input().strip()

n = int(input())
word_dict = set(input().split())

length = len(s)

# dp[i] = True if s[0:i] can be segmented
dp = [False] * (length + 1)
dp[0] = True

for i in range(1, length + 1):
    for word in word_dict:
        word_len = len(word)

        if word_len <= i and dp[i - word_len]:
            if s[i - word_len:i] == word:
                dp[i] = True
                break

print("YES" if dp[length] else "NO")
