def quickSort(src):
    n = len(src)
    if n <= 1:
        return src
    pivot = src[-1]
    g1 = []
    g2 = []
    for i in range(0, n - 1):
        if src[i] < pivot:
            g1.append(src[i])
        else:
            g2.append(src[i])
    return quickSort(g1) + [pivot] + quickSort(g2)

# a = [5, 3, 7, 6, 2, 1, 4]
# print(quickSort(a))
