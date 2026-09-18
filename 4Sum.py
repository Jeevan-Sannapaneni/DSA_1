

"""
Problem: 4Sum
Difficulty: Medium

Problem Statement:
Given an integer array and a target value, find all unique
quadruplets [a, b, c, d] such that:

a + b + c + d = target

The solution must not contain duplicate quadruplets.

Input:
First line: N (number of elements)
Second line: N space-separated integers
Third line: Target value

Output:
Print all unique quadruplets, one per line.
If no quadruplet exists, print -1.

Time Complexity: O(N^3)
Space Complexity: O(1) excluding the output
"""

n = int(input())
nums = list(map(int, input().split()))
target = int(input())

nums.sort()
result = []

for i in range(n - 3):

    if i > 0 and nums[i] == nums[i - 1]:
        continue

    for j in range(i + 1, n - 2):

        if j > i + 1 and nums[j] == nums[j - 1]:
            continue

        left = j + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[j] + nums[left] + nums[right]

            if total == target:
                result.append(
                    (nums[i], nums[j], nums[left], nums[right])
                )

                left += 1
                right -= 1

                # Skip duplicate values
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < target:
                left += 1
            else:
                right -= 1

if result:
    for quadruplet in result:
        print(*quadruplet)
else:
    print(-1)
