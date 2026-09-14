

"""
Problem: Sliding Window Maximum
Difficulty: Hard

Problem Statement:
Given an array of integers and a window size k, find the maximum
value in every contiguous window of size k.

Input:
First line: N (number of elements)
Second line: N space-separated integers
Third line: Window size k

Output:
Print the maximum value from each window.

Time Complexity: O(N)
Space Complexity: O(K)
"""

from collections import deque

n = int(input())
nums = list(map(int, input().split()))
k = int(input())

dq = deque()
result = []

for i in range(n):
    # Remove indices outside the current window
    while dq and dq[0] <= i - k:
        dq.popleft()

    # Remove smaller elements from the back
    while dq and nums[dq[-1]] <= nums[i]:
        dq.pop()

    dq.append(i)

    # Window is ready once we have k elements
    if i >= k - 1:
        result.append(nums[dq[0]])

print(*result)
