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

#Print Keypad Combination
def print_keypad(ques,ans):
    if len(ques) == 0:
        print(ans)
        return 
    
    ch = int(ques[0])
    for i in arr[ch]:

        print_keypad(ques[1:], ans + i)


print_keypad(s,'')