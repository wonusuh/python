def mergeSort(a):
    n = len(a)
    if n <= 1: # 자료가 한 개이면 종료한다.
        return a
    mid = n // 2 # 그룹을 나누어 각각 병합 정렬
    g1 = mergeSort(a[:mid])
    g2 = mergeSort(a[mid:])
    result = [] #두 그룹을 하나로 병합
    while g1 and g2: # 자료가 남아있는 동안 반복
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    while g1: # 아직 남아있는 자료들을 추가
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result # (이 return은 어디에 걸리는가? : def에 걸린다.)

d = [10, 3, 8, 6, 7, 4, 5, 2, 3, 1, 33]
print(mergeSort(d))
