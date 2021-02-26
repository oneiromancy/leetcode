def mergeAlternately(word1, word2):
    result = ''

    for idx, letter in enumerate(word1):
        result += letter

        if idx < len(word2):
            result += word2[idx]

    if len(word2) > len(word1):
        result += word2[len(word1):]

    return result


mergeAlternately('abcde', 'pqr')
