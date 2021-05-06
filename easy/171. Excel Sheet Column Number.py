def titleToNumber(columnTitle):
    total = 0
    size = len(columnTitle)

    for i in range(size):
        total += 26 ** (size - i - 1) * (ord(columnTitle[i]) - 64)

    return total

print(titleToNumber('AB'))

# A => B => ... => Z 26
# AA => AB => ... => AZ 26
# BA => BB => ... => BZ 26
# .
# .
# .
# ZA => ZB => ... => ZZ 26
# AAA => AAB => ... => AAZ 26
# ABA => ABB => ... => ABZ 26