# Given a string s which represents an expression, evaluate this expression and return its value. 
# The integer division should truncate toward zero.
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Example 1:

# Input: s = "3+2*2"
# Output: 7
# Example 2:

# Input: s = " 3/2 "
# Output: 1
# Example 3:

# Input: s = " 3+5 / 2 "
# Output: 5

# 302+12/3-8

def calculate(s: str) -> int:
    stack = []
    current_number = 0
    ope = '+'

    for i, char in enumerate(s):
        if char.isnumeric():
            current_number = current_number*10 + int(char)
        if char in '+-*/' or i == len(s)-1:
            if ope == '+':
                stack.append(current_number)
            elif ope == '-':
                stack.append(-current_number)
            elif ope == '*':
                stack.append(stack.pop() * current_number)
            elif ope == '/':
                stack.append(int(stack.pop()/current_number))
            current_number = 0
            ope = char

    return sum(stack)

print(calculate("3+2*2"))
print(calculate("3+5/2"))
