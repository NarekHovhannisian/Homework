# String Power
def power(s, k):
    if k >= 0:
        return s * k
    else:
        a = s[:len(s) // -k]
        if a * -k == s:
            return a
        else:
            return "undefined"
