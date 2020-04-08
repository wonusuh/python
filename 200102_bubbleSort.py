def bubbleSort():
    for i in range(len(lst)):
        k = 0
        for j in range(len(trg)):
            if trg[j] > lst[i]:
                k = j
                break
        trg.insert(k, lst[i])

lst = [9, 5, 1, 8, 2, 3, 4, 6, 7]
trg = []

bubbleSort()
print(trg)
