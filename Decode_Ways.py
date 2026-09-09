

"""
Problem: Decode Ways
Difficulty: Medium

Problem Statement:
A message contains digits from '1' to '26'.
Each number can be decoded as a letter:

1 -> A
2 -> B
...
26 -> Z

Given a string of digits, find the total number of ways to decode it.

A '0' cannot be decoded by itself.

Input:
A string containing digits.

Output:
Print the number of possible decodings.

Time Complexity: O(N)
Space Complexity: O(1)
"""

s = input().strip()

if not s or s[0] == '0':
    print(0)
else:
    prev2 = 1
    prev1 = 1

    for i in range(1, len(s)):
        current = 0

        # Decode the current digit individually
        if s[i] != '0':
            current += prev1

        # Decode the current and previous digits together
        two_digit = int(s[i - 1:i + 1])

        if 10 <= two_digit <= 26:
            current += prev2

        prev2 = prev1
        prev1 = current

    print(prev1)
