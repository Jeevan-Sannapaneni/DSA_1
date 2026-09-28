

"""
Problem: Koko Eating Bananas
Difficulty: Medium

Problem Statement:
Koko has several piles of bananas and must finish eating all
bananas within H hours.

If Koko eats at speed k bananas per hour, she chooses one pile
per hour and eats up to k bananas from that pile.

Find the minimum integer eating speed that allows her to finish
all bananas within H hours.

Input:
First line: N (number of banana piles)
Second line: N space-separated pile sizes
Third line: H (maximum number of hours)

Output:
Print the minimum eating speed.

Time Complexity: O(N log M)

Where:
N = number of piles
M = maximum pile size

Space Complexity: O(1)
"""

n = int(input())
piles = list(map(int, input().split()))
h = int(input())

left = 1
right = max(piles)

answer = right

while left <= right:
    speed = left + (right - left) // 2

    hours_needed = 0

    for pile in piles:
        # Ceiling division: ceil(pile / speed)
        hours_needed += (pile + speed - 1) // speed

    if hours_needed <= h:
        answer = speed
        right = speed - 1
    else:
        left = speed + 1

print(answer)
