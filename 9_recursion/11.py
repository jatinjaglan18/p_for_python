s = input()

def permutations(ques,ans):
    if len(ques) == 0:
        print(ans)
        return
    
    for i in range(len(ques)):
        ch = ques[i]
        rques = ques[:i] + ques[i+1:]
        permutations(rques,ans+ch)

permutations(s,'')