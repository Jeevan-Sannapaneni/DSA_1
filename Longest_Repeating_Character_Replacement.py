
"""
Problem: Longest Repeating Character Replacement
Difficulty: Medium

Problem Statement:
Given a string containing uppercase English letters and an integer k,
you can replace at most k characters with any other uppercase letter.

Find the length of the longest substring that can be transformed into
a substring containing only one repeated character.

Input:
First line: A string s
Second line: An integer k

Output:
Print the maximum possible length.

Time Complexity: O(N)
Space Complexity: O(1)
"""

s = input().strip()
k = int(input())

frequency = {}
left = 0
max_frequency = 0
answer = 0

for right in range(len(s)):
    frequency[s[right]] = frequency.get(s[right], 0) + 1

    max_frequency = max(max_frequency, frequency[s[right]])

    # Characters that need to be replaced
    replacements = (right - left + 1) - max_frequency

    while replacements > k:
        frequency[s[left]] -= 1
        left += 1

        max_frequency = max(frequency.values())

        replacements = (right - left + 1) - max_frequency

    answer = max(answer, right - left + 1)

print(answer)
