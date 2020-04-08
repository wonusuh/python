src = [5, 4, 1, 2, 3]
trg = []
print(src, trg)

def myFn1(x):
    tmp = x.pop(0)
    tmpLst = []
    tmpLst.append(tmp)
    return tmpLst
trg = myFn1(src)
print(src, trg)

def myFn2(x):
    tmp = x.pop(0) # 0번 인덱스의 값을 추출
    # tmp의 값이 trg[0]과 비교해 위치를 정한다.
    tmpLst = trg[:] # [5]
    if tmp < trg[0]:
        tmpLst.insert(0, tmp)
    else:
        tmpLst.insert(1, tmp)
    return tmpLst    
trg = myFn2(src)
print(src, trg)

def myFn3(x):
    tmp = x.pop(0)
    minIdx = 0
    tmpLst = trg[:]
    for index in range(len(tmpLst)):
        if tmp < tmpLst[index]:
            if tmpLst[index] < tmpLst[minIdx]:
                minIdx = index
        else:
            minIdx = index + 1 
    tmpLst.insert(minIdx, tmp)
    return tmpLst
trg = myFn3(src)
print(src, trg)

def myFn4(x):
    tmp = x.pop(0)
    minIdx = 0
    tmpLst = trg[:]
    for index in range(len(tmpLst)):
        if tmp < tmpLst[index]:
            if tmpLst[index] < tmpLst[minIdx]:
                minIdx = index
        else:
            minIdx = index + 1 
    tmpLst.insert(minIdx, tmp)
    return tmpLst
trg = myFn4(src)
print(src, trg)

def myFn5(x):
    tmp = x.pop(0)
    minIdx = 0
    tmpLst = trg[:]
    for index in range(len(tmpLst)):
        if tmp < tmpLst[index]:
            if tmpLst[index] < tmpLst[minIdx]:
                minIdx = index
        else:
            minIdx = index + 1 
    tmpLst.insert(minIdx, tmp)
    return tmpLst
trg = myFn5(src)
print(src, trg)
