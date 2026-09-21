"""
Problem: Maximum Sum Circular Subarray
Difficulty: Medium

Problem Statement:
Given a circular integer array, find the maximum possible sum
of a non-empty contiguous subarray.

Since the array is circular, the subarray can wrap from the
end of the array back to the beginning.

Input:
First line: N (number of elements)
Second line: N space-separated integers

Output:
Print the maximum circular subarray sum.

Time Complexity: O(N)
Space Complexity: O(1)
"""

n = int(input())
nums = list(map(int, input().split()))

total_sum = sum(nums)

# Standard Kadane's algorithm for maximum subarray
current_max = maximum_sum = nums[0]

# Kadane's algorithm for minimum subarray
current_min = minimum_sum = nums[0]

for num in nums[1:]:
    current_max = max(num, current_max + num)
    maximum_sum = max(maximum_sum, current_max)

    current_min = min(num, current_min + num)
    minimum_sum = min(minimum_sum, current_min)

# If all elements are negative, the circular result cannot
# be obtained by removing the minimum subarray.
if maximum_sum < 0:
    print(maximum_sum)
else:
    circular_sum = total_sum - minimum_sum
    print(max(maximum_sum, circular_sum))
