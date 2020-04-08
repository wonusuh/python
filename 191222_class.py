num = 7
print(num)
num = 9
print(num)
def changeNum(p):
    global num
    num = p
changeNum(1)
print(num)
