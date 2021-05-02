def romanToInt(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    arabic = 0
    size = len(s)

    for idx in range(size):
        if idx + 1 < size and roman[s[idx]] < roman[s[idx + 1]]:
            arabic -= roman[s[idx]]
        else:
            arabic += roman[s[idx]]

    return arabic

print(romanToInt("III"))

