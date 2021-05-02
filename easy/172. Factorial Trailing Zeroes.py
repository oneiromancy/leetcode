def trailingZeroes(n):
    i = 1
    nums = []
    factors_of_five = n

    while factors_of_five > 1:
        factors_of_five = n // (5 ** i)
        nums.append(factors_of_five)
        i += 1

    return sum(nums)

print(trailingZeroes(30))
