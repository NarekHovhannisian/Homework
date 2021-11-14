def findWords(words):
    first = "qwertyuiop"
    second = "asdfghjkl"
    third = "zxcvbnm"
    result = []
    for word in words:
        from_first = [letter in first for letter in word.lower()]
        if False not in from_first:
            result.append(word)
        from_second = [letter in second for letter in word.lower()]
        if False not in from_second:
            result.append(word)
        from_third = [letter in third for letter in word.lower()]
        if False not in from_third:
            result.append(word)
    return result
