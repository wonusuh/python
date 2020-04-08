lst = ['Tom', 'Jerry', 'Ben', 'Tom']
newlst = []
for i in range(len(lst) - 1):  
    for j in range(i + 1, len(lst)):
        source = lst[i]
        target = lst[j]
        bl = source == target
        if bl:
            newlst.append(source)
        print('%s(%s) vs %s(%s) = %s' %(i, source, j, target, bl))
print('same name = %s' %newlst)
