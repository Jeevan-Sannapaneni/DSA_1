

"""
Problem: Min Stack
Difficulty: Medium

Problem Statement:
Design a stack that supports the following operations:

1. PUSH x  - Add x to the stack.
2. POP     - Remove the top element.
3. TOP     - Print the top element.
4. MIN     - Print the minimum element in the stack.

All operations should run in O(1) time.

Input:
First line: Q (number of operations)
Next Q lines: One operation per line.

Output:
For TOP and MIN operations, print the corresponding value.
For invalid TOP, POP, or MIN operations on an empty stack,
print EMPTY.

Time Complexity: O(Q)
Space Complexity: O(Q)
"""

q = int(input())

stack = []
min_stack = []

for _ in range(q):
    operation = input().split()

    command = operation[0]

    if command == "PUSH":
        value = int(operation[1])

        stack.append(value)

        if not min_stack:
            min_stack.append(value)
        else:
            min_stack.append(min(value, min_stack[-1]))

    elif command == "POP":
        if stack:
            stack.pop()
            min_stack.pop()
        else:
            print("EMPTY")

    elif command == "TOP":
        if stack:
            print(stack[-1])
        else:
            print("EMPTY")

    elif command == "MIN":
        if min_stack:
            print(min_stack[-1])
        else:
            print("EMPTY")
