
"""
Problem: Valid Parentheses
Difficulty: Easy

Problem Statement:
Given a string containing only '(', ')', '{', '}', '[' and ']',
determine whether the brackets are valid.

A valid string must satisfy:
1. Every opening bracket has a matching closing bracket.
2. Brackets are closed in the correct order.
3. Every closing bracket matches its corresponding opening bracket.

Input:
A single string containing brackets.

Output:
Print YES if the brackets are valid.
Otherwise, print NO.

Time Complexity: O(N)
Space Complexity: O(N)
"""

s = input().strip()

stack = []

matching = {
    ')': '(',
    '}': '{',
    ']': '['
}

for char in s:

    if char in "({[":
        stack.append(char)

    else:
        if not stack or stack[-1] != matching[char]:
            print("NO")
            break

        stack.pop()

else:
    print("YES" if not stack else "NO")
