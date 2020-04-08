# with open('./ggd.txt', 'w')as f:
#     for i in range(2, 10):
#         for j in range(1, 10):
#             i * j
#             data = "%sx%s=%s\n" %(i, j, i * j)
#             f.write(data)

data = ""
for i in range(0, 3):
    if i > 0:
        data += "\n\n"
    for j in range(1, 10):
        for k in range(2, 5):
            if k % 3 == 1:
                newLine = "\n"
            else:
                newLine = "\t"
            dan = i * 3 + k
            if dan <= 9:
                data += str(dan) + "x" + str(j) + "=" + str(dan * j) + newLine
            else:
                data += newLine

f = open("./ggd2.txt", "w")
f.write(data)
f.close()
