n = [14, 37, 76, 59, 41, 28, 51, 48, 11]
minIdx = 0
minX = n[minIdx]

for idx in range(1, len(n)):
    print('%d and %d' %(minX, n[idx]))
    if minX > n[idx]:
        minIdx = idx
        minX = n[minIdx]
        # print('minX is small')

print('min index is %s' %minIdx)
