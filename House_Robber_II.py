"""
Problem: House Robber II
Difficulty: Medium

Problem Statement:
The houses are arranged in a circle.

Each house contains some amount of money.
You cannot rob two adjacent houses.

Since the first and last houses are also adjacent,
you cannot rob both of them.

Find the maximum amount of money you can rob.

Input:
First line: N (number of houses)
Second line: N space-separated amounts of money

Output:
Print the maximum amount of money that can be robbed.

Time Complexity: O(N)
Space Complexity: O(1)
"""

n = int(input())
money = list(map(int, input().split()))


def rob_linear(houses):
    prev2 = 0
    prev1 = 0

    for amount in houses:
        current = max(prev1, prev2 + amount)
        prev2 = prev1
        prev1 = current

    return prev1


if n == 0:
    print(0)

elif n == 1:
    print(money[0])

else:
    # Case 1: Exclude the last house
    case1 = rob_linear(money[:-1])

    # Case 2: Exclude the first house
    case2 = rob_linear(money[1:])

    print(max(case1, case2))
