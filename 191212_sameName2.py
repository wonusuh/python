lst = ['Tom', 'Jerry', 'Ben', 'Tom']
newlst = []
for src in lst:
    for tgt in newlst:
        print('target: %s' %tgt)
    newlst.append(src)
    print('source: %s' %src)
print(newlst)
