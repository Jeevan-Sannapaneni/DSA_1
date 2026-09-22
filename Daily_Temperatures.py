

"""
Problem: Daily Temperatures
Difficulty: Medium

Problem Statement:
Given an array of daily temperatures, find for each day how many
days you have to wait until a warmer temperature occurs.

If no warmer day exists, output 0 for that day.

Input:
First line: N (number of days)
Second line: N space-separated temperatures

Output:
Print the number of days to wait for a warmer temperature
for each day.

Time Complexity: O(N)
Space Complexity: O(N)
"""

n = int(input())
temperatures = list(map(int, input().split()))

answer = [0] * n
stack = []

for i in range(n):

    # Resolve previous days whose temperature is lower
    while stack and temperatures[i] > temperatures[stack[-1]]:
        previous_day = stack.pop()
        answer[previous_day] = i - previous_day

    stack.append(i)

print(*answer)
