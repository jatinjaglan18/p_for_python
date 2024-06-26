#Get Keypad combination
arr = ['?!','abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz','.;']
s = input()
def keyPad(s):
    if len(s) == 0:
        res = ['']
        return res
    
    ch = int(s[0])
    l = keyPad(s[1:])
    res = []
    for i in arr[ch]:
        for j in l:
            res.append(i + j)
    return res

print(keyPad(s))

