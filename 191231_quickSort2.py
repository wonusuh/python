lst = [5, 3, 7, 6, 2, 1, 4]

def quickSort(src, step = 0):
    n = len(src)
    i = 0
    j = n - 2
    p = n - 1

    if i == p:
        return

    while src:
        pv = src[p]
        iv = src[i]
        jv = src[j]

        if i == j or i > j:
            lst[step + p] = src[p] = iv
            lst[step + i] = src[i] = pv
            p = i
            quickSort(src[:p], step)
            quickSort(src[p + 1:], step + p + 1)
            return

        if pv < iv and iv < jv:
            j = j - 1
        elif jv < pv and pv < iv:
            lst[step + i] = src[i] = jv
            lst[step + j] = src[j] = iv
            i = i + 1
            j = j - 1
        else:
            i = i + 1

quickSort(lst)
print(lst)
