a = [5, 3, 7, 6, 2, 1, 4]
pivot = a[len(a) - 1]
left = []
same = []
right = []

for i in a:
    if i < pivot:
        left.append(a.pop(0))
    elif i == pivot:
        same.append(a.pop(0))
    else:
        right.append(a.pop(0))

print(a, left, same, right)
