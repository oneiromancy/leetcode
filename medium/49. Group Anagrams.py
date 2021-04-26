def groupAnagrams(strs):
    groups = {}

    for word in strs:
        alpha_word = ''.join(sorted(word))

        if alpha_word in groups:
            groups[alpha_word].append(word)
        else:
            groups[alpha_word] = [word]

    return [value for key, value in groups.items()]

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:

# Input: strs = [""]
# Output: [[""]]

# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

 

# Constraints:

#     1 <= strs.length <= 104
#     0 <= strs[i].length <= 100
#     strs[i] consists of lower-case English letters.

