# Beautiful Binary String
def beautifulBinaryString(b):
    res = 0
    lst = list(b)
    for i in range(1, len(b)-1):
        if lst[i] == '1' and lst[i - 1] == lst[i + 1] == '0':
            res += 1
            lst[i + 1] = '1'
            i += 2
    return res
