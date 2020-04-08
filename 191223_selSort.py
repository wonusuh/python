d = [2, 4, 5, 1, 3]

def findMinIndex(lst):
    print(lst)
    minIdx = 0
    n = len(d)
    for i in range(1, n):
        if d[minIdx] > d[i]:
            minIdx = i
            print(minIdx)
    return minIdx

def selSort(d):
    result = []
    while d:
        minIdx = findMinIndex(d)
        value = d.pop(minIdx)
        result.append(value)
    return
print(selSort(d))

# findMinIndex(d)
# d.pop(3) # 최소값 인덱스를 제거
# findMinIndex(d)
# d.pop(0) # 최소값 인덱스를 제거
# findMinIndex(d)
# d.pop(2) # 최소값 인덱스를 제거
# findMinIndex(d)
# d.pop(0) # 최소값 인덱스를 제거
