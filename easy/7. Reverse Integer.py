def reverse(x):
    reverse_num = ''
    string_x = str(x)

    for i in range(len(string_x) - 1, -1, -1):
        if string_x[i] == '-':
            reverse_num = string_x[i] + reverse_num
        else:
            reverse_num += string_x[i]

    reverse_num = int(reverse_num)

    if abs(reverse_num) > abs(2**31):
        return 0
    else:
        return reverse_num

print(reverse(-120))

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321

# Example 2:

# Input: x = -123
# Output: -321

# Example 3:

# Input: x = 120
# Output: 21

# Example 4:

# Input: x = 0
# Output: 0
