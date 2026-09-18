

"""
Problem: 3Sum
Difficulty: Medium

Problem Statement:
Given an integer array, find all unique triplets [a, b, c]
such that:

a + b + c = 0

The solution must not contain duplicate triplets.

Input:
First line: N (number of elements)
Second line: N space-separated integers

Output:
Print all unique triplets, one per line.
If no triplet exists, print -1.

Time Complexity: O(N^2)
Space Complexity: O(1) excluding the output
"""

n = int(input())
nums = list(map(int, input().split()))

nums.sort()
result = []

for i in range(n - 2):

    # Skip duplicate first elements
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    left = i + 1
    right = n - 1

    while left < right:
        total = nums[i] + nums[left] + nums[right]

        if total == 0:
            result.append((nums[i], nums[left], nums[right]))

            left += 1
            right -= 1

            # Skip duplicates
            while left < right and nums[left] == nums[left - 1]:
                left += 1

            while left < right and nums[right] == nums[right + 1]:
                right -= 1

        elif total < 0:
            left += 1
        else:
            right -= 1

if result:
    for triplet in result:
        print(*triplet)
else:
    print(-1)
