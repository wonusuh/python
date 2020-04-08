lst = [6, 4, 5, 1, 2, 3]
trg = []

for i in range(len(lst)): # for item in lst:
    print(i)
    # trg.append(item)
    # 4, 6이 있는 경우 5를 넣으려면 6(1)일때만 True
    if i == 0:
        trg.append(lst[i])
        continue
    for j in range(len(trg)):
        if trg[j] > lst[i]:
            trg.insert(j, lst[i])
            break
    print(trg)
