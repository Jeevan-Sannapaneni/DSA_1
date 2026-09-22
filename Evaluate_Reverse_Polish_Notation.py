

"""
Problem: Evaluate Reverse Polish Notation
Difficulty: Medium

Problem Statement:
Given an arithmetic expression in Reverse Polish Notation (RPN),
evaluate the expression.

Valid operators are:
+, -, *, /

Division between two integers should truncate toward zero.

Input:
First line: N (number of tokens)
Second line: N space-separated tokens

Output:
Print the result of the expression.

Time Complexity: O(N)
Space Complexity: O(N)
"""

n = int(input())
tokens = input().split()

stack = []

for token in tokens:
    if token not in {"+", "-", "*", "/"}:
        stack.append(int(token))
    else:
        b = stack.pop()
        a = stack.pop()

        if token == "+":
            result = a + b
        elif token == "-":
            result = a - b
        elif token == "*":
            result = a * b
        else:
            # Truncate division toward zero
            result = int(a / b)

        stack.append(result)

print(stack[-1])
