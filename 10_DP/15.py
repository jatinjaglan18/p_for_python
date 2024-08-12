#Count susequence of form a+ b+ c+

string = input()

def count_sub(s):
    a = 0
    ab = 0
    abc = 0

    for i in s:
        if i == 'a':
            a = (2 * a) + 1
        elif i == 'b':
            ab = (2 * ab) + a
        elif i == 'c':
            abc = (2 * abc) + ab
    return abc
print(count_sub(string))