def plusOne(digits):
    digits = map(str, digits)
    digits = ''.join(digits) 
    digits = int(digits) + 1

    return [int(digit) for digit in str(digits)]

print(plusOne([9]))
