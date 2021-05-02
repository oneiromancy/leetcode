def isPalindrome(s):
    s = ''.join([ch.lower() for ch in s if ch.isalnum()])

    return s == ''.join(reversed(s))

print(isPalindrome("A man, a plan, a canal: Panama"))