#Print Encodings
s = input()
#print(chr(ord('a')- 1 + 12))

def encodings(ques,ans):
    if len(ques) == 0:
        print(ans)
        return
    elif len(ques) == 1:
        if ques[0] == '0':
            return 
        else:
            ch = ques[0]
            print(ans + chr(ord('a')-1 + int(ch)))
        
    else:
        ch = ques[0]
        roq = ques[1:]
        if ques[0] == '0':
            return 
        else:
            ch = ques[0]
            encodings(roq, ans + chr(ord('a')-1 + int(ch)))

        ch12 = ques[:2]
        roq12 = ques[2:]

        if int(ch12) <= 26:
            encodings(roq12, ans + chr(ord('a')-1 + int(ch12)))

encodings(s,'')