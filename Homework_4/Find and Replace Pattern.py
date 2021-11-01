# Find and Replace Pattern
def findAndReplacePattern(words, pattern):
    res = []
    for word in words:
        dict1, dict2 = {}, {}
        check = True
        for w, p in zip(word, pattern):
            if w not in dict1:
                dict1[w] = p
            if p not in dict2:
                dict2[p] = w
            if dict1[w] != p or dict2[p] != w:
                check = False
                break
        if check:
            res.append(word)
    return res
