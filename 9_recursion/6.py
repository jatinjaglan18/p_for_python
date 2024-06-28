#get subsequence
str = input()
def subSequence(s):
    if len(s) == 0:
        res =['']
        return res
    ch = s[0]
    l = subSequence(s[1:])
    res = []
    for i in l:
        res.append(i)
        res.append(ch + i)
    return res
print(subSequence(str))

#print subsequence
def subsequence(ques, ans):
    if len(ques) == 0:
        print(ans)
        return
    ch = ques[0]
    subsequence(ques[1:],ans + ch)
    subsequence(ques[1:],ans + '')

subsequence(str,'')