words = ['e', 'k', 'o', 'o', 'r', 'a', 'r', 'e', 'k']
newWords = []

def checkDupl(a, b):
    isDupl = False
    if(a == b):
        isDupl = True
    return isDupl

for i in words:
    isAdd = True
    for j in newWords:
        if checkDupl(i, j):
            isAdd = False

    if isAdd:
        newWords.append(i)

print(newWords)
