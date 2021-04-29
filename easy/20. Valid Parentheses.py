def isValid(s):
    stack = []
    d = {'(': ')', '[': ']', '{': '}'}

    for ch in s:
        if ch in d.keys():
            stack.append(ch)
        elif len(stack) > 0 and ch == d[stack.pop()]:
            continue
        else:
            return False

    if len(stack) > 0:
        return False
    else:
        return True

print(isValid("(("))

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.

 

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false

# Example 4:

# Input: s = "([)]"
# Output: false

# Example 5:

# Input: s = "{[]}"
# Output: true

 
        