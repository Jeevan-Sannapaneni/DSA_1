

"""
Problem 107: Edit Distance

Difficulty: Medium

Problem Statement:
Given two strings, find the minimum number of operations
required to convert the first string into the second.

Allowed operations:
1. Insert a character
2. Delete a character
3. Replace a character

Input:
String 1
String 2

Output:
Minimum number of operations.

Time Complexity: O(N * M)
Space Complexity: O(N * M)
"""

word1 = input().strip()
word2 = input().strip()

n = len(word1)
m = len(word2)

dp = [[0] * (m + 1) for _ in range(n + 1)]

# Converting a string into an empty string requires
# deleting all its characters.
for i in range(n + 1):
    dp[i][0] = i

# Converting an empty string into a string requires
# inserting all its characters.
for j in range(m + 1):
    dp[0][j] = j


for i in range(1, n + 1):
    for j in range(1, m + 1):

        if word1[i - 1] == word2[j - 1]:

            dp[i][j] = dp[i - 1][j - 1]

        else:

            insert = dp[i][j - 1]
            delete = dp[i - 1][j]
            replace = dp[i - 1][j - 1]

            dp[i][j] = 1 + min(
                insert,
                delete,
                replace
            )

print(dp[n][m])
