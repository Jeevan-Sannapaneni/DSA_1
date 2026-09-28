

"""
Problem: Find Minimum in Rotated Sorted Array
Difficulty: Medium

Problem Statement:
A sorted array of distinct integers has been rotated at an
unknown position.

Find the minimum element in the array.

Input:
First line: N (number of elements)
Second line: N space-separated integers

Output:
Print the minimum element.

Time Complexity: O(log N)
Space Complexity: O(1)
"""

n = int(input())
nums = list(map(int, input().split()))

left = 0
right = n - 1

while left < right:
    mid = left + (right - left) // 2

    if nums[mid] > nums[right]:
        # Minimum is in the right half
        left = mid + 1
    else:
        # Minimum is at mid or in the left half
        right = mid

print(nums[left])
