"""
Problem: Binary Search
Difficulty: Easy

Problem Statement:
Given a sorted array of integers and a target value, find the
index of the target using binary search.

If the target does not exist, print -1.

Input:
First line: N (number of elements)
Second line: N space-separated integers in sorted order
Third line: Target value

Output:
Print the index of the target using zero-based indexing.
Print -1 if the target is not present.

Time Complexity: O(log N)
Space Complexity: O(1)
"""

n = int(input())
nums = list(map(int, input().split()))
target = int(input())

left = 0
right = n - 1

while left <= right:
    mid = left + (right - left) // 2

    if nums[mid] == target:
        print(mid)
        break

    elif nums[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

else:
    print(-1)
