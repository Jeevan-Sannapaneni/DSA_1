"""
Problem: Search in Rotated Sorted Array
Difficulty: Medium

Problem Statement:
A sorted array has been rotated at an unknown position.

Given the rotated array and a target value, find the index of
the target.

All elements are assumed to be distinct.

Input:
First line: N (number of elements)
Second line: N space-separated integers
Third line: Target value

Output:
Print the zero-based index of the target.
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

    # Left half is sorted
    if nums[left] <= nums[mid]:

        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    # Right half is sorted
    else:

        if nums[mid] < target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1

else:
    print(-1)
