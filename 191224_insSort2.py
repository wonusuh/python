src = [5, 4, 3, 2, 1]

def insSort(x):
    target = []
    while x:
        tmp = x.pop(0)
        minIdx = 0
        for index in range(len(target)):
            if tmp < target[index]:
                if target[index] < target[minIdx]:
                    minIdx = index
            else:
                minIdx = index + 1
        target.insert(minIdx, tmp)
    return target
trg = insSort(src)
print(trg)
