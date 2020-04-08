a = [71, 49, 33, 21, 86, 93]
x = a[0]

for i in a:
    if i < x:
        x = i

print("minimum is %s." %x, "its index number is %s." %(a.index(x)))

# -----------------------------------------------

# a = [71, 49, 33, 21, 86, 93]
# min = 71
# minIdx = 0
# for i in range(1, len(a)):
#     if min > a[i]:
#         min = a[i]
#         minIdx = i
# print(minIdx)
