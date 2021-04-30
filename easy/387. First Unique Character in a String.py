def firstUniqChar(s):
    d = {}

    for ch in s:
        d[ch] = 1 if ch not in d else d[ch] + 1

    for idx, ch in enumerate(s):
        if d[ch] == 1:
            return idx

    return -1
    

print(firstUniqChar("aabb"))

# Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0

# Example 2:

# Input: s = "loveleetcode"
# Output: 2

# Example 3:

# Input: s = "aabb"
# Output: -1

 

# Constraints:

#     1 <= s.length <= 105
#     s consists of only lowercase English letters.


