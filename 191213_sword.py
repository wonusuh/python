words = ['e', 'k', 'o', 'o', 'r', 'a', 'r', 'e', 'k']
duplWords = []

def checkDupl(a, b):
    isDupl = False
    if(a == b):
        isDupl = True
    return isDupl

for i in range(len(words)):
    curChar = words[i]
    if len(words) > 1:
        tempList = words[i + 1:]
        for j in range(len(tempList)):
            if checkDupl(curChar, tempList[j]):
                duplWords.append(words[i])
for k in duplWords:
    words.remove(k)

print(words)
