def strStr(haystack, needle):
    if haystack == needle or not needle:
        return 0

    n = len(needle)
    
    for i in range(len(haystack) - n + 1):
        if haystack[i:i+n] == needle:
            return i

    return -1

    
print(strStr("hello", "ll"))

# Input: haystack = "hello", needle = "ll"
# Output: 2