def longestCommonPrefix(strs):
    if not strs:
        return ""

    shortest_word = min(strs,key=len)

    for i, ch in enumerate(shortest_word):
        for other in strs:
            if other[i] != ch:
                return shortest_word[:i]
                
    return shortest_word

print(longestCommonPrefix(["flower","flow","flight"]))
